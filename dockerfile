FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev curl \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip \
  && curl -fsSL https://d2lang.com/install.sh | sh -s --

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD python3 -u ./api.py