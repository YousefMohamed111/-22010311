# Base image
FROM python:alpine

WORKDIR /app

COPY . .

RUN pip install NLTK

CMD ["python", "script.py"]