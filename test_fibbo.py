import unittest
import app
import pydevd
pydevd.settrace('192.168.1.7',
                port=4567,
                stdoutToServer=True,
                stderrToServer=True,
                suspend=False)

class TestFibbo(unittest.TestCase):
    def test_pass_fibbo_one_or_zero_returns_one(self):
        for i in [0, 1]:
            fibbo_value = app.fibbo(i)
            self.assertEqual(fibbo_value, 1)

if __name__ == '__main__':
    unittest.main()