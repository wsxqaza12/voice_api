import requests
from io import BytesIO
from pydub import AudioSegment
from .config import MODEL_PATHS

class VoiceAPI:
    def __init__(self, api_base_url, api_port):
        self.base_url = f"{api_base_url}:{api_port}"
        self.model_paths = MODEL_PATHS
        self.current_model = None

    def set_model(self, model_name):
        if model_name not in self.model_paths:
            print(f"Error: Model '{model_name}' not found.")
            return False

        self.current_model = self.model_paths[model_name]
        # self._set_refer_audio(self.current_model["refer_audio"])
        self._set_gpt_weights(self.current_model["gpt_weights"])
        self._set_sovits_weights(self.current_model["sovits_weights"])
        return "Model setting completed"

    def _set_refer_audio(self, refer_audio_path):
        endpoint = f"{self.base_url}/set_refer_audio"
        params = {"refer_audio_path": refer_audio_path}
        response = requests.get(endpoint, params=params)
        print(f"Set refer audio: {response.json()}")
        return response.json()

    def _set_gpt_weights(self, weights_path):
        endpoint = f"{self.base_url}/set_gpt_weights"
        params = {"weights_path": weights_path}
        response = requests.get(endpoint, params=params)
        print(f"Set GPT weights: {response.json()}")
        return response.json()

    def _set_sovits_weights(self, weights_path):
        endpoint = f"{self.base_url}/set_sovits_weights"
        params = {"weights_path": weights_path}
        response = requests.get(endpoint, params=params)
        print(f"Set SoVITS weights: {response.json()}")
        return response
    
    def _tts_api(self,
                     text,
                     text_lang="zh",
                     ref_audio_path=None, 
                     aux_ref_audio_paths=None,                     
                     prompt_text=None, 
                     prompt_lang="zh", 
                     top_k=15, 
                     top_p=1, 
                     temperature=1, 
                     text_split_method="cut1", 
                     batch_size=1, 
                     batch_threshold=0.75, 
                     split_bucket=True, 
                     speed_factor=1.0, 
                     streaming_mode=False, 
                     seed=1235, 
                     parallel_infer=True, 
                     repetition_penalty=1.35):
        
        endpoint = f"{self.base_url}/tts"
        data = {
            "text": text,
            "text_lang": text_lang,
            "ref_audio_path": self.current_model["refer_audio"],
            "aux_ref_audio_paths": aux_ref_audio_paths if aux_ref_audio_paths else [],
            "prompt_text": self.current_model["prompt_text"],
            "prompt_lang": prompt_lang,
            "top_k": top_k,
            "top_p": top_p,
            "temperature": temperature,
            "text_split_method": text_split_method,
            "batch_size": batch_size,
            "batch_threshold": batch_threshold,
            "split_bucket": split_bucket,
            "speed_factor": speed_factor,
            "streaming_mode": streaming_mode,
            "seed": seed,
            "parallel_infer": parallel_infer,
            "repetition_penalty": repetition_penalty
        }
        response = requests.post(endpoint, json=data)
        print(f"Synthesize audio response: {response.status_code}. Text:{text}")
        return response
    
    def _split_text(self, text, max_length=100):
        """Split text into paragraphs not exceeding max_length, with priority given to '. ' and then split."""
        paragraphs = []
        current_paragraph = ""
        
        for char in text:
            current_paragraph += char
            if len(current_paragraph) >= max_length and char == '。':
                paragraphs.append(current_paragraph.strip())
                current_paragraph = ""

        if current_paragraph:
            paragraphs.append(current_paragraph.strip())

        return paragraphs
    
    def tts_generate(self, text, **kwargs):
        """Split the text, call API to synthesize audio for each text segment, and merge all audio segments."""
        # 切分文本為段落
        paragraphs = self._split_text(text)
        audio_segments = []

        for paragraph in paragraphs:
            response = self._tts_api(paragraph, **kwargs)
            if response.status_code == 200:
                audio_segments.append(AudioSegment.from_file(BytesIO(response.content)))
            else:
                print("Error in obtaining audio for paragraph.")

        # 合併所有音頻片段
        combined_audio = AudioSegment.empty()
        for segment in audio_segments:
            combined_audio += segment

        # 保存合併後的音頻
        # combined_audio.export("combined_audio.wav", format="wav")
        # print("All audio segments have been merged into 'combined_audio.wav'.")
        
        return combined_audio