FROM python:3.8

LABEL maintainer="caue.guedes91@gmail.com"

WORKDIR /usr/src/app
COPY requirements.txt  ./

RUN pip install -r requirements.txt

COPY . /usr/src/app/

CMD [ "bash"]