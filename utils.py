"""
Reused procedures across problems.
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

