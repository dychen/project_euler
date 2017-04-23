"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

PANDIGITAL_DIGITS = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

def is_pandigital(num_str):
    return (set(num_str) == PANDIGITAL_DIGITS
            and len(num_str) == len(PANDIGITAL_DIGITS))

def try_multiples(n):
    result = ''
    multiplicand = 1
    while len(result) < 9:
        result += str(n * multiplicand)
        multiplicand += 1
        if is_pandigital(result):
            return int(result)
    return None

def largest_pandigital_multiple(limit=9999):
    """
    9999 is the largest possible integer that could for a concatenated 9-digit
    pandigital multiple. Anything larger would be more than 9 digits (10000 =>
    10000 x 1 || 10000 x 2 => 1000020000
    """
    n = 1
    largest = 0
    while n <= limit:
        pandigital = try_multiples(n)
        if pandigital:
            print n, pandigital
            if pandigital > largest:
                largest = pandigital
        n += 1
    return largest

print largest_pandigital_multiple()
