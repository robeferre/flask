FROM python:3.6.5-alpine3.7

#RUN apk update && \
#    apk upgrade && \
#    apk add mariadb-dev && \
#    apk add --no-cache mariadb-dev build-base && \
#    apk add gcc && \
#    apk add libc-dev && \
#    apk add git && \
#    apk add htop

ADD . /opt/app

WORKDIR  /opt/app

RUN apk --no-cache add --virtual build-dependencies \
      build-base \
      py-mysqldb \
      gcc \
      libc-dev \
      libffi-dev \
      mariadb-dev \
      linux-headers \
      git \
      && pip install -r requirements.txt \
      && rm -rf .cache/pip \
      && apk del build-dependencies

EXPOSE 8080

CMD ["python", "manage.py runserver"]
