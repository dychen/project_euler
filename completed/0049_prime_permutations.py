# SLOW! Algorithm is O(n^3)...

def generate_primes(maximum):
    nums = range(2, maximum)
    primes = []
    while len(nums) > 1:
        curr = nums[0]
        nums = nums[1:]
        primes.append(curr)
        i = 1
        prod = curr * i
        while prod <= nums[-1]:
            if prod in nums:
                nums.remove(prod)
            i += 1
            prod = curr * i
    return primes

def four_digit_primes(prime_list):
    for i in range(len(prime_list)):
        if prime_list[i] > 999:
            return prime_list[i:]

fd_primes = four_digit_primes(generate_primes(10000))

for i in range(len(fd_primes)):
    print fd_primes[i]
    for j in range(i+1, len(fd_primes)):
        for k in range(j+1, len(fd_primes)):
            if fd_primes[k] - fd_primes[j] == fd_primes[j] - fd_primes[i]:
                if set(str(fd_primes[i])) == set(str(fd_primes[j])) and \
                   set(str(fd_primes[j])) == set(str(fd_primes[k])):
                    print fd_primes[i], fd_primes[j], fd_primes[k]