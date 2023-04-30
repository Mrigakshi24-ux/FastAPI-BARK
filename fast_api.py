from fastapi import FastAPI, Request, Form
from fastapi.responses import FileResponse, RedirectResponse
import glob
import os
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi.staticfiles import StaticFiles
from pydub import AudioSegment
from fastapi.responses import StreamingResponse

app = FastAPI(debug=True)
#app.mount("/static", StaticFiles(directory="static", html=True), name="static")
templates = Jinja2Templates(directory='Templates')

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse('form.html', {'request':request})

@app.post("/process")
async def processing(textInput: str = Form(...)):
    # return f'{textInput}'
    url_ = glob.glob(os.path.join('./static', '*.wav'))[0]
    output_file = './static/demo.mp3'
    sound = AudioSegment.from_wav(url_)
    sound.export(output_file, format="mp3")
    url_ = glob.glob(os.path.join('./static', '*.mp3'))[0]

    response = RedirectResponse(url = 'demo.mp3')
    # return FileResponse("demo.mp3", media_type="audio/mp3")
    return response


    # return FileResponse(output_file, media_type="audio/mpeg")

@app.get("/audio")
async def audio(request: Request):
    return templates.TemplateResponse('audio.html', {'request':request})
# @app.post("/")

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)