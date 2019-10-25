# docker build -t osdu-quickstart-python-srv .

FROM python:3.7.4

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY src/ ./

EXPOSE 8080

CMD gunicorn entry_api:api -b 0.0.0.0:8080
