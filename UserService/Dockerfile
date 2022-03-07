FROM python:3.9.10-buster

COPY . /userService
WORKDIR /userService

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["run.py" ]