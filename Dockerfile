FROM ubuntu:latest 
WORKDIR /app

RUN apt update -y
RUN apt upgrade -y

RUN apt install python3 python3-pip build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev -y
COPY . /app
# COPY ./sub/*.txt sub/
RUN pip3 install discord
RUN pip3 install requests
RUN pip3 install aiohttp
RUN pip3 install youtube_dl
Run apt install ffmpeg
ENV token=ODI1NzI2MjEyOTY1MDA3Mzgw.YGCHdg.uuOpiHb79T4ZiUQNguoUZ6JOals
CMD ["bash","run.sh"]
