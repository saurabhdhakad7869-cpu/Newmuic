FROM python:3.10-slim-buster

# System dependencies install karein
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends ffmpeg git python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# App directory setup
COPY . /app/
WORKDIR /app/

# Requirements install karein
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Bot start command
CMD python3 -m AnieXEricaMusic
