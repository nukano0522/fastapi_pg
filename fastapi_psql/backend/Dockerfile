# FROM ubuntu:20.04
# RUN apt-get -y update && apt-get -y install software-properties-common \
# && add-apt-repository ppa:deadsnakes/ppa && apt -y install python3.10 && apt -y install python3-pip

FROM python:3.10-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /src
COPY api ./src

RUN pip3 install --upgrade pip
RUN pip3 install fastapi
RUN pip3 install "uvicorn[standard]"
RUN pip3 install requests
RUN pip3 install SQLAlchemy

# psycopg2のインストール
# RUN apt install python3-dev libpq-dev
RUN pip3 install psycopg2

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002", "--reload"]
