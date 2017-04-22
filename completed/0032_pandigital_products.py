"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""

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

def generate_pandigital_products(pandigital_str):
    """
    Generate all (multiplicand, multiplier, product) tuples from a pandigital
    string.

    Args:
        pandigital_str [str]: String representation of a pandigital number,
                              e.g. '123456789'
    Yields:
        [tuple]: All tuples ([int], [int], [int]) repesenting 2-partitions of
                 the string, e.g. ((1, 2, 3456789), (1, 23, 456789), ...)
    """
    for i, _ in enumerate(pandigital_str):
        multiplicand, rem = pandigital_str[:i], pandigital_str[i:]
        for j, _ in enumerate(rem):
            multiplier, product = rem[:j], rem[j:]
            if multiplicand and multiplier and product:
                yield (int(multiplicand), int(multiplier), int(product))

def pandigital_products():
    def verify(multiplicand, multiplier, product):
        return multiplicand * multiplier == product

    results = set([])
    for pandigital in generate_pandigitals():
        for m1, m2, product in generate_pandigital_products(pandigital):
            if verify(m1, m2, product):
                results.add(product)
    return list(results)

print sum(pandigital_products())
