FROM alpine

COPY src-python/requirements.txt /tmp/requirements.txt

RUN apk add --no-cache python3 \
	&& pip3 install -r /tmp/requirements.txt

WORKDIR /data


## Build
# docker build . -f Dockerfile.python -t testenv:python
# cd /home/src-python

## Run Unit Tests:
# docker run --tty -v $(pwd):/data testenv:python python3 -m unittest discover example-py-unittest/

## Run Doctests:
# docker run --tty -v $(pwd):/data testenv:python python3 -m doctest example-py-doctest/com/automationpanda/example/*.py

## Run Pytest:
# docker run --tty -v $(pwd):/data --workdir /data/example-py-pytest testenv:python python3 -m pytest


## Aliases:
# alias python-unittest='docker run --tty -v $(pwd):/data testenv:python python3 -m unittest discover example-py-unittest/'
# alias python-doctest='docker run --tty -v $(pwd):/data testenv:python python3 -m doctest example-py-doctest/com/automationpanda/example/*.py'
# alias python-pytest='docker run --tty -v $(pwd):/data --workdir /data/example-py-pytest testenv:python python3 -m pytest'
#
# python-unittest
# python-doctest
# python-pytest
