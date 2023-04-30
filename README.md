# FastAPI-BARK
Generating audio outputs from text prompts using BARK

The file structure is as follows: 
- fast_api.py
- Templates
  - form.html
- model.py
- Dockerfile

The fast_api.py contains all the routes.
The form.html contains the basic structure for the webpage.
The model.py will return the audio output after receiving a text prompt.
The dockerfile helps in building the docker image. 

FastAPI routes:

- '/' (home route): This route will render an HTML file 'form.html'. It consists of a text input which will be the input to the language model.
- 'process' (process route): After clicking the submit button on the home page, the HTML page will call this route 'process' which will process the input using BARK module and it the response from the module will be saved as an audio file and it will be redirected to a different route 'audio'.
- 'audio' (audio route): This route 'audio' displays the saved audio file on the webpage.

STEPS TO RUN THE DOCKERFILE
- Clone the repository
  - git clone 
- Build the docker image
  - docker build -t 'imageName'.
- Run the docker image as a container
  - docker run 'imageName'
  
After the docker is running succesfully, navigate to the link provided on the terminal. In order to test the web application, provide an input in the text box and click submit to listen to the AI-Generated audio file.
  
