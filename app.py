import pydevd
pydevd.settrace('192.168.1.7',
                port=4567,
                stdoutToServer=True,
                stderrToServer=True,
                suspend=False)
def fibbo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibbo(n-1) + fibbo(n-2)
