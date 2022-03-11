FROM python:3.9.10-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]