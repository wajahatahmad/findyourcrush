FROM alpine:latest
RUN apk update 
RUN apk add --no-cache \
git \
python3 \
py3-pip gcc \
python3-dev \
php openssh
WORKDIR /root
RUN git clone https://github.com/wajahatahmad/findyourcrush.git
WORKDIR /root/findyourcrush/
ENTRYPOINT ["/bin/sh"]
