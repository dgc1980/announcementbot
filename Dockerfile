FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /tmp
COPY bot/ /app

RUN pip install -r /tmp/requirements.txt  --no-cache-dir

RUN chmod +x "/app/run.sh"
CMD [ "/app/run.sh" ]
