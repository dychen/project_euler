"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from utils import generate_primes

PRIMES = generate_primes(1000000)
PRIMES_SET = set(PRIMES)
longest_sequence, sequence_length = [], 0

# Truncating primes to the first 1000 primes is a heuristic to speed up the
# algorithm. No proof that this gives the correct answer (but it does in this
# case).
for i, _ in enumerate(PRIMES[:1000]):
    for j in range(i+1, len(PRIMES[:1000])):
        if sum(PRIMES[i:j]) in PRIMES_SET and j - i > sequence_length:
            #print len(PRIMES[i:j]), sum(PRIMES[i:j])
            longest_sequence, sequence_length = PRIMES[i:j], len(PRIMES[i:j])
print sum(longest_sequence)

