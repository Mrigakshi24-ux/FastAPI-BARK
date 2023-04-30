FROM python:3.9
ADD ./ .
COPY ./ .

RUN pip install -r requirements.txt
RUN install git+https://github.com/suno-ai/bark.git

EXPOSE 8000
CMD ["python", "fast_api.py"]
