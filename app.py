

def fibbo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibbo(n-1) + fibbo(n-2)
