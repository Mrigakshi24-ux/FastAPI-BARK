from fastapi import FastAPI, Request, Form
from typing import Annotated
import glob
import os
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi.staticfiles import StaticFiles
from pydub import AudioSegment
import os
from bark import SAMPLE_RATE, generate_audio
from IPython.display import Audio
from scipy.io.wavfile import write as write_wav

def returnAudioFile(text):
    audio_array = generate_audio(text)
    #Audio(audio_array, rate=SAMPLE_RATE)
    # os.makedirs('/static')
    
    write_wav("./static/audio.wav", SAMPLE_RATE, audio_array)



app = FastAPI(debug=True)
app.mount("/static", StaticFiles(directory="static", html=True), name="static")
templates = Jinja2Templates(directory='Templates')

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse('form.html', {'request':request})

@app.post("/process")
async def processing(textInput: str = Form(...)):
    returnAudioFile(textInput)
    #url_ = glob.glob(os.path.join('.\static', '*.wav'))[0]

    # output_file = r'static\demo.mp3'

    # sound = AudioSegment.from_wav(r"\static\audio.wav") 
    # sound.export(output_file, format='mp3')
    
    response = RedirectResponse(url = '/audio')
    return response

@app.post('/audio')
async def audio(request: Request):
    return templates.TemplateResponse('audio.html', {'request': request})



if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)