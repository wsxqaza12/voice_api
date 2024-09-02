# VoiceAPI

This package provides a Python wrapper for the Voice API, allowing easy interaction with the GPT-SoVITS voice synthesis system.

## Installation

```
pip install voice_api-1.0.0-py3-none-any.whl
```

## Usage

```python
from voice_api import VoiceAPI

api = VoiceAPI(api_base_url="http://203.145.215.7", api_port="7860")
api.set_model("woman1")  # or "man1", "woman2", "man2"
audio = api.tts_generate("新聞的講稿")
# audio.export("audio_test.wav", format="wav")
```

## Running Tests

```
python -m unittest discover tests
```