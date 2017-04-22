# Euler discovered the remarkable quadratic formula:
#  n^2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive
# values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is
# divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
# divisible by 41.
# The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80
# primes for the consecutive values n = 0 to 79. The product of the
# coefficients, -79 and 1601, is -126479.
# Considering quadratics of the form:
#  n^2 + an + b, where |a| < 1000 and |b| < 1000
#  where |n| is the modulus/absolute value of n
#  e.g. |11| = 11 and |-4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n = 0.

# Approach:
#   Brute force, with the following simplification:
#   Note that for the equation to be satisfied for n = 0, b must be a positive
#   prime.

# Returns the number of consecutive primes produced by n^2 + an + b starting
# from n = 0.
def consecutive_primes(a, b, primes):
    n = 0
    res = n ** 2 + n * a + b
    while res in primes:
        n += 1
        res = n ** 2 + n * a + b
    return n

def find_quadratic_primes(A, B, primes):
    largest = { 'a': A, 'b': B, 'num_primes': -1 }
    bset = [p for p in primes if p < B]
    for a in range(-A+1, A):
        for b in bset:
            num = consecutive_primes(a, b, primes)
            if num > largest['num_primes']:
                largest['num_primes'] = num
                largest['a'] = a
                largest['b'] = b
    return largest['a'] * largest['b']

# Helper functions

# Returns a list of primes less than n.
def generate_primes(n):
    nums = range(2, n)
    primes = set([])
    while len(nums) > 0:
        prime = nums[0]
        primes.add(prime)
        nums = [num for num in nums if num % prime != 0]
    return primes

if __name__ == '__main__':
    ABOUND = 1000
    BBOUND = 1000
    primes = generate_primes(10000)
    print find_quadratic_primes(ABOUND, BBOUND, primes)
