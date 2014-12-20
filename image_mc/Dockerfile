FROM ubuntu:14.04
MAINTAINER despiegk <kristof@incubaid.com>
#we started from https://github.com/phusion/baseimage-docker
#lots of credits to phusion

ENV HOME /root
RUN ["mkdir","-p","/build"]
ADD . /build

RUN /build/prepare.sh && \
    /build/system_services.sh && \
    /build/utilities.sh && \
    /build/jumpscaleprepare.sh && \
    /build/cleanup.sh \

CMD ["/sbin/my_init"]
