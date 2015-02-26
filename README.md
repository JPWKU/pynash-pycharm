===========================================
Remote Debugging with PyCharm (and Vagrant)
===========================================
### Hello!!! My name is Jeremy Phelps and I'm from Bowling Green, KY (about an hour north of here)
### Super glad to be hanging with PyNash and look forward to learning a ton
### I spend a lot of my time building things as a member of [Dell Cloud Manager](http://software.dell.com/products/cloud-manager/) on the backend systems team. 
### Other times I can be found mountain biking with my family and in pursuit of the perfect hot wing.
### My motivations for presenting at PyNash are:
    1. Get out of my comfort zone and in front of people (the scariest place).
    2. Talk about PyCharm because I think it's cool (and I wanna know some more about it).
    3. Be a part of a great community.


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
  * Make sure you have Vagrant plugin installed (Pycharm -> Preferences -> plugins -> vagrant)
  * Set up remote interpreter (point to the one we have just created) (File -> Default Settings -> Default Project -> interpreter) 
  * Edit configuration to set up remote debugger (Edit config-> + -> Python Remote Debug)
  * Fill in name, hostname, port, and path mapping (remember the port)
  * You can now start the debug server

5. Go back to your VM and kick off a script or test suite:
  * Copy the following snippet into the script that you want to debug
  * ``` import pydevd
pydevd.settrace(<local ip of host machine>, port=4567, stdoutToServer=True, stderrToServer=True) ```
  * Now you can kick off your script/test-suite and you will see the process connect to the PyCharm debugger
  * It will pause on the first executable statement that it comes to if you pass ``` suspend=True ``` to settrace 
  * Otherwise you can now set breakpoints and step through/step out.  Even just going step by step to get a nice visual of how your program executes.
  * ``` cd /<projectdirectory>/es-ex-pyagent/tests/ ```

