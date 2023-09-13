FROM python:3.8-slim-bullseye
RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN apt-get update -y && apt-get install build-essential libpq-dev python-dev python3-dev -y
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools wheel
RUN pip install -r requirements.txt
RUN chmod +x ./start.sh
CMD ["./start.sh"]