#!/bin/bash
set -e
source /build/buildconfig
set -x


$minimal_apt_get_install mc python-git git ssh python2.7 python-requests python-apt openssl ca-certificates wget rsync -y
cd /tmp;wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
cd /tmp;python get-pip.py

apt-get install libmhash2 libpython-all-dev python-redis python-hiredis -y

#change passwd
echo -e "gig1234\ngig1234" | (passwd root)



