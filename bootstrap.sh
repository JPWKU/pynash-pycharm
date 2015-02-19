#!/usr/bin/env bash

apt-get -y update
apt-get install -y python-virtualenv
virtualenv --no-site-packages /opt/pynashenv
source /opt/pynashenv/bin/activate

