# A unit fraction contains 1 in the numerator. The decimal representation of
# the unit fractions with denominators 2 to 10 are given:
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
# seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle
# in its decimal fraction part.

# Approach:
# Prime unit fractions with repeating decimals have a one-to-one relationship
# with cyclic numbers. The repeating cycle is given by:
# (10^(p-1) - 1) / p, where p is relatively prime to 10.
# Note that the repeating cycle can have at most p-1 digits.
# If there is no cycle in (10^(p-1) - 1) / p, p is called a full reptend prime.
def longest_recurring_cycle(n):
    longest_cycle = -1
    longest_prime = None
    primes = generate_primes(n)
    primes.remove(2)
    primes.remove(5)
    for prime in primes:
        cycle = (10 ** (prime-1) - 1) / prime
        # We have to 0-pad the cycle to p-1 digits.
        length = cycle_length(str(cycle).zfill(prime-1))
        if length > longest_cycle:
            longest_cycle = length
            longest_prime = prime
    return longest_prime

# Helper functions

# Returns a list of primes less than n.
def generate_primes(n):
    nums = range(2, n)
    primes = []
    while len(nums) > 0:
        prime = nums[0]
        primes.append(prime)
        nums = [num for num in nums if num % prime != 0]
    return primes

# Returns longest cycle length of a potentially repeating string s.
# Approach:
#   Find all indices of the first character of the input string.
#   For each index, check if the index-length substrings are the same.
#   If all substrings are the same, there is a cycle of length index, but there
#   might also be subcycles in that cycle, so recursively check the substring
#   until there are no more cycles, in which case the length of the string is
#   returned.
def cycle_length(s):
    c = s[0]
    indices = [i for i, e in enumerate(s) if e == c and i != 0]
    indices.reverse()
    for idx in indices:
        cycles = [s[:i*idx] == s[idx:(i+1)*idx] for i in range(1, len(s)/idx)]
        if len(cycles) > 0 and reduce(lambda x, y: x and y, cycles) == True:
            return cycle_length(s[:idx])
    return len(s)

if __name__ == '__main__':
    BOUND = 1000
    print longest_recurring_cycle(BOUND)
