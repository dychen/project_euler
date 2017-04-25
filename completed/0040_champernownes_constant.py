"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""

def generate_decimal_str(length=1000000):
    s = ''
    n = 1
    while len(s) <= length:
        s += str(n)
        n += 1
    return s[:length]

def find_constant():
    print d[0], d[9], d[99], d[999], d[9999], d[99999], d[999999]
    return reduce(lambda x, y: int(x) * int(y),
                  [d[0], d[9], d[99], d[999], d[9999], d[99999], d[999999]])

print find_constant()
