MODEL_PATHS = {
    "woman1": {
        "refer_audio": "/home/ubuntu/voice/woman1/example.wav",
        "gpt_weights": "/home/ubuntu/GPT-SoVITS/GPT_weights_v2/woman_voice1-e50.ckpt",
        "sovits_weights": "/home/ubuntu/GPT-SoVITS/SoVITS_weights_v2/woman_voice1_e24_s768.pth",
        "prompt_text": "而这呢也是选战开跑之后，两位候选人首度的正面交锋，我们看一下呢这场辩论会可以说是呢是创下了好几个历史上的纪录喔"
    },
    "man1": {
        "refer_audio": "/home/ubuntu/voice/man1/1example.wav",
        "gpt_weights": "/home/ubuntu/GPT-SoVITS/GPT_weights_v2/man_voice1-e50.ckpt",
        "sovits_weights": "/home/ubuntu/GPT-SoVITS/SoVITS_weights_v2/man_voice1_e24_s768.pth"
    }
}

API_BASE_URL = "http://127.0.0.1"
API_PORT = 9880