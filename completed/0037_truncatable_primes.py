"""
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from utils import find_next_prime, generate_primes

NUM_TRUNCATABLE_PRIMES = 11

def is_truncatable_prime(n, primes_set):
    def is_prime(prime):
        return prime in primes_set

    if n in set([2, 3, 5, 7]):
        return False

    n_str = str(n)
    for i in range(len(n_str)):
        prefix, suffix = n_str[i:], n_str[:i]
        if ((prefix and not is_prime(int(prefix)))
            or suffix and not is_prime(int(suffix))):
            return False
    return True

def find_truncatable_primes():
    prime_set = set([])
    truncatable_primes_list = []

    for prime in find_next_prime():
        prime_set.add(prime)
        if is_truncatable_prime(prime, prime_set):
            # print 'Truncatable prime', prime
            truncatable_primes_list.append(prime)
            if len(truncatable_primes_list) == NUM_TRUNCATABLE_PRIMES:
                return truncatable_primes_list

print sum(find_truncatable_primes())
