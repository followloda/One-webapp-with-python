FROM tiangolo/uwsgi-nginx-flask:python3.6

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ENV STATIC_INDEX 1

COPY ./app /app
