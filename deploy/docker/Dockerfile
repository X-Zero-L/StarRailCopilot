FROM python:3.10.10-slim

WORKDIR /app

COPY . /app

RUN apt update && apt install -y git adb python3-opencv

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 22367

CMD [ "python", "gui.py" ]