"""
Reused procedures across problems.
"""
import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for m in xrange(2, int(math.ceil(math.sqrt(n)))+1):
        if n % m == 0:
            return False
    return True

def generate_primes(n):
    """
    Generate all primes up to and including @n
    Args:
        n [int]: The largest number to consider.
    Return:
        [list]: List of primes [2, 3, 5, ...]
    """
    if n < 2:
        return []
    is_prime_arr = [True for _ in xrange(0, n+1)]
    is_prime_arr[0] = False
    is_prime_arr[1] = False
    i = 2
    while i < len(is_prime_arr):
        if is_prime_arr[i]:
            j = i * 2
            while j < len(is_prime_arr):
                is_prime_arr[j] = False
                j += i
        i += 1
    return [idx for idx, e in enumerate(is_prime_arr) if e]

def generate_pandigitals(ndigits=9):
    """
    Recursively generate string representations of all pandigitals from
    123456789 to 987654321. There are 9! (362880) of them.

    Args:
        ndigits [str]: Generate pandigitals from (1..ndigits)
    Return:
        [list]: List of pandigital strings ['123456789', '123456798', ...]
    """
    def generate_pandigitals_rec(digits, rem_digits):
        if len(rem_digits) == 0:
            return [''.join([str(x) for x in digits])]
        else:
            results = []
            for i, digit in enumerate(rem_digits):
                results += generate_pandigitals_rec(
                    digits + [digit], rem_digits[:i] + rem_digits[i+1:]
                )
            return results

    return generate_pandigitals_rec([], [x for x in range(1, ndigits+1)])

