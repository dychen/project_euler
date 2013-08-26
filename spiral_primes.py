import math

def is_prime(n):
    for m in range(2, int(math.sqrt(n))):
        if n % m == 0:
            return False
    return True

def check(depth, num_primes):
    lower = depth ** 2
    upper = (depth + 2) ** 2
    inter = (upper - lower) / 4
    array = range(upper-inter, lower, -inter)
    for n in array:
        if is_prime(n):
            num_primes += 1
    return num_primes

def main():
    num_primes = 3
    num_checked = 5
    depth = 3
    while (float(num_primes) / num_checked > 0.10):
        num_primes = check(depth, num_primes)
        num_checked += 4
        depth += 2
        print num_primes, num_checked
    return depth

print main()