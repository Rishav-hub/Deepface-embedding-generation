FROM python:3.8-slim-buster
COPY . /deepface_embedding
WORKDIR /deepface_embedding
RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -r requirements.txt
RUN pip install -e .
CMD ["python","app.py"]