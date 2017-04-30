def fib(n):
    f = [0] * (n + 1)
    f[1] = 1
    for i in xrange(2, n+1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

def anotherfib(n):
    return additiveseq(n, 0, 1)

def additiveseq(n, t0, t1):
    if n == 0:
        return t0
    if n == 1:
        return t1
    return additiveseq(n - 1, t1, t0 + t1)

print anotherfib(6)    
