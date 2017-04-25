"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?
"""

from utils import find_next_prime

def factorize(n, prime_list):
    """
    Return a set of computed resolved prime factors.
    E.g., factorize(644) => set([23, 4, 7]) # 2^2 * 7 * 23
    """
    primes = set([])
    for next_prime in prime_list:
        if n == 1:
            break
        if n % next_prime == 0:
            next_factor = 1
            while n % next_prime == 0:
                n /= next_prime
                next_factor *= next_prime
            primes.add(next_factor)
    return primes

def find_consecutive_n_distinct_prime_factors(count=4):
    def has_n_distinct_prime_factors(factors_list):
        """
        Args:
            factors_list [list]: [
                [[factor 1], [factor 2], ...],
                [[factor 3], [factor 4], ...],
                ...
            ]
        """
        # Check if there are @count distinct primes in each sublist
        if not all([len(factor_list) == count for factor_list in factors_list]):
            return False
        # Check if all primes in all sublists are distinct
        flattened = [factor for factor_list in factors_list
                     for factor in factor_list]
        if len(flattened) == len(set(flattened)):
            return True
        return False

    prime_list = [] # Memoize for faster factorization
    numbers = [x for x in range(2, count+2)]
    factors = [factorize(x, [2, 3]) for x in range(2, count+2)]
    n = count + 2
    # Generate primes
    for next_prime in find_next_prime():
        prime_list.append(next_prime)
        # Walk up to the next prime
        while n < next_prime:
            numbers = numbers[1:] + [n]
            factors = factors[1:] + [factorize(n, prime_list)]
            if has_n_distinct_prime_factors(factors):
                return (numbers, factors)
            n += 1

numbers, factors = find_consecutive_n_distinct_prime_factors(4)
print numbers[0]
