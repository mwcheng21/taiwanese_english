import gradio as gr
from gtts import gTTS
import subprocess
import os
api_key = os.getenv("HF_API_KEY") # Get your API key from huggingface.co

def inference(audio, model):
    en_hk_two_pass = gr.Interface.load("huggingface/facebook/xm_transformer_unity_en-hk", api_key=api_key)
    hk_en_two_pass = gr.Interface.load("huggingface/facebook/xm_transformer_unity_hk-en", api_key=api_key)
    if model == "xm_transformer_unity_en-hk":
        out_audio = en_hk_two_pass(audio)
    else:
        out_audio = hk_en_two_pass(audio)
    return out_audio 

def text_to_speech(text):
    print("Generating english speech...")
    language = 'en'
        
    myobj = gTTS(text=text, lang=language, slow=True)
    myobj.save("/tmp/english_audio.mp3")

def speech_to_hk():
    print("Converting to hokkien ...")
    tmpfile_location = inference("/tmp/english_audio.mp3", "xm_transformer_unity_en-hk")
    return tmpfile_location

sentence = 'Hello, how are you? I want to eat some tofu pudding and beef noodle soup. I am very hungry.'

text_to_speech(sentence)
hk_audio = speech_to_hk()
outfile_location = "./output.mp3"
subprocess.run(["mv", hk_audio, outfile_location])