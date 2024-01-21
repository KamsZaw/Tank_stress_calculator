FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN apt-get update
RUN apt-get install vim -y
RUN mkdir -p /home/cloud

COPY . /app

CMD ["python","calc_stress.py"]