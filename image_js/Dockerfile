FROM despiegk:mc
MAINTAINER despiegk <kristof@incubaid.com>
#we started from https://github.com/phusion/baseimage-docker
#lots of credits to phusion

ENV HOME /root
RUN ["mkdir","-p","/build"]
ADD . /build

RUN /build/jumpscale.sh && \
    /build/cleanup.sh \

CMD ["/sbin/my_init"]
