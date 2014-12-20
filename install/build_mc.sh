# apt-get update
# apt-get autoremove -y
# apt-get -f install -y
# apt-get upgrade -y

set -ex

apt-get install mc curl git ssh python2.7 python-requests -y

curl https://raw.githubusercontent.com/Jumpscale/docker/master/install/bootstrap_mc.py | python 