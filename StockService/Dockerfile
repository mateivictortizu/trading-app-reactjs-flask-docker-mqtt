FROM python:3.9.10-buster

COPY . /stockService
WORKDIR /stockService

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["run.py" ]