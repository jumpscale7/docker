#!/bin/bash
set -e
source /build/buildconfig
set -x


curl https://raw.githubusercontent.com/Jumpscale/jumpscale_core7/master/install/install_python_web.sh | bash


