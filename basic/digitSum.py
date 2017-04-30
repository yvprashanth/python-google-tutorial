def digitSum(n):
    if n >= 0 and n < 10:
        return n
    if n < 0:
        n = n * -1
        return digitSum(n)
    else:
        lastDigit = n % 10
        return lastDigit + digitSum(n/10)

print digitSum(-1729)