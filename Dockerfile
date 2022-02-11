FROM python:3.8-slim-bullseye

RUN apt update &&\
    apt -y install gnupg2 &&\
    apt -y install vim bash-completion wget &&\
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - &&\
    echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" | tee  /etc/apt/sources.list.d/pgdg.list &&\
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |  apt-key add - &&\
    apt -y install postgresql-13 postgresql-client-13 &&\
    apt -y install postgis postgresql-13-postgis-3 &&\
    apt -y install osm2pgsql

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "index.py"]