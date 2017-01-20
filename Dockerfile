FROM python:3.4

MAINTAINER Denis Yakovlev <denis.honig.yakovlev@gmail.com>

ADD . /opt/hosttrackerlib/
WORKDIR /opt/hosttrackerlib/

RUN pip install -r requirements.txt

CMD ["bash", "-c"]
