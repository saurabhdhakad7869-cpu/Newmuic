FROM python:3.10-slim-bullseye

# Sab kuch update aur install karein
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends ffmpeg git python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# App folder setup
COPY . /app/
WORKDIR /app/

# Requirements file install karein
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Bot ko run karne ki command
CMD python3 -m AnieXEricaMusic
