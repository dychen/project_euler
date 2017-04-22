"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""

from utils import is_prime, generate_pandigitals

def largest_pandigital():
    for digits in range(9, 0, -1):
        for i, pandigital in enumerate(generate_pandigitals(digits)[::-1]):
            if is_prime(int(pandigital)):
                return pandigital

print largest_pandigital()
