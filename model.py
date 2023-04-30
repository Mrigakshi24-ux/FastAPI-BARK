from bark import SAMPLE_RATE, generate_audio
from IPython.display import Audio
from scipy.io.wavfile import write as write_wav
import os

def returnAudioFile(text):
    audio_array = generate_audio(text)
    Audio(audio_array, rate=SAMPLE_RATE)
    os.makedirs('static')
    write_wav("/static/audio.wav", SAMPLE_RATE, audio_array)


text = """ Buenos días Miguel. Tu colega piensa que tu alemán es extremadamente malo. 
    But I suppose your english isn't terrible."""

returnAudioFile(text)   