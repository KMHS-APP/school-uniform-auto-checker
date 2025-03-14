FROM python:alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENV TZ=Asia/Seoul

ENTRYPOINT ["python", "main.py"]
