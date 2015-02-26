#!/usr/bin/env bash

apt-get -y update
apt-get -y install unzip
apt-get install -y python-virtualenv
virtualenv --no-site-packages /opt/pynashenv
source /opt/pynashenv/bin/activate
cd /opt/pynashenv/lib/python2.7/site-packages
cp /vagrant/pycharm-debug.egg .
unzip pycharm-debug.egg 
echo 'export PYDEV_IP='$1 >> /tmp/pydevd
echo 'export PYDEV_PORT=4567' >> /tmp/pydevd
cd /vagrant 
pip install -r requirements.txt
