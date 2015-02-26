import sys

import pydevd
import os


try:
    ip = os.environ['PYDEV_IP']
    port = os.environ['PYDEV_PORT']
except KeyError:
    print "You must set PYDEV_IP and PYDEV_PORT"
    sys.exit(1)


pydevd.settrace(ip,
                port=int(port),
                stdoutToServer=True,
                stderrToServer=True,
                suspend=True)


def fibbo(n):
    if n == 0 or n == 1:
        return 2
    else:
        return fibbo(n-1) + fibbo(n-2)
