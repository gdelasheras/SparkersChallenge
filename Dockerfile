FROM python:3.7-buster

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /code
COPY *.py /code/
COPY stats_app /code/stats_app
WORKDIR /code
EXPOSE 8080

ENTRYPOINT [ "python", "main.py" ]