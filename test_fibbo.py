import sys
import os
import unittest
import app
import pydevd

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


class TestFibbo(unittest.TestCase):
    def test_pass_fibbo_one_or_zero_returns_one(self):
        for i in [0, 1]:
            fibbo_value = app.fibbo(i)
            self.assertEqual(fibbo_value, 1)

if __name__ == '__main__':
    unittest.main()