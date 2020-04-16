FROM ubuntu

RUN apt update && apt install -y git gcc make libpcap-dev \

RUN git clone https://github.com/AstroTech/ecosystem-example-c /tmp \
    && cd /tmp \
    && ./configure \
    && make \
    && make install


## -----


FROM alpine

RUN apk add --no-cache git gcc musl-dev libpcap-dev make

RUN git clone https://github.com/AstroTech/ecosystem-example-c /tmp \
    && cd /tmp \
    && ./configure \
    && make \
    && make install
