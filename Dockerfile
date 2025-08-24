FROM python:3.13-alpine

COPY . /app
RUN cd /app && pip3 install -r requirements.txt

EXPOSE 8081

WORKDIR /app

ENTRYPOINT ["python3","vulnerable-flask-app.py"]
