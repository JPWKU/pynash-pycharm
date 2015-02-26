===========================================
Remote Debugging with PyCharm (and Vagrant)
===========================================
### Hi!!! My name is Jeremy Phelps and I'm from Bowling Green, KY (about an hour north of here)
### Super glad to be hanging with PyNash and look forward to learning a ton
### I spend a lot of my time building things as a member of [Dell Cloud Manager](http://software.dell.com/products/cloud-manager/) on
### the backend systems team.  Other times I can be found mountain biking with my family and 
### in pursuit of the perfect hot wing.

## Setup Instructions for PyCharm on Mac 0SX

This assumes you have [PyCharm Professional Edition](http://www.jetbrains.com/pycharm/buy/) 
and [Vagrant](https://www.vagrantup.com/downloads.html) installed

1. Go into the project directory
  * ``` cd ~/pynash-pycharm/ ```

2. Copy pycharm-debug.egg into the project directory 
  * ``` cp /Applications/PyCharm.app/pycharm-debug.egg .  ```

3. Start up VM with provided Vagrantfile
  * The project root will be mapped to /vagrant directory in the VM once started. 
  *  ``` vagrant up ``` 
  *  ``` vagrant ssh ```
  *  ``` sudo -i ```
  *  ``` apt-get update ```
  *  ``` apt-get install python-virtualenv```
  *  ``` cd /vagrant ```

  * Create and activate virtualenv and install deps
  *  ``` virtualenv --no-site-packages /opt/pynashenv ```
  *  ``` source /opt/pynashenv/bin/activate ```
  *  ``` pip install -r requirements.txt ```

  * Install unzip then cp and unzip pycharm-debug.egg into virtualenv site-packages
  *  ``` apt-get install unzip ```
  *  ``` cd /opt/pynash-pycharm/lib/python2.7/site-packages/ ```
  *  ``` cp /vagrant/pycharm-debug.egg . ``` 
  *  ``` unzip pycharm-debug.egg ```

4. Setup PyCharm
  * Make sure you have Vagrant plugin installed
  * Set up remote interpreter (point to the one we have just created) 
5. Now back in the shell of your vagrant machine you can run:
  * ``` cd /<projectdirectory>/es-ex-pyagent/tests/ ```

