# Approach:
#   Note that x^2 - D y^2 = 1 can be rewritten as
#   y^2 = (x^2 - 1) / D
#   y^2 = (x+1)(x-1) / D
#   So, we only need to check x where (x+1) or (x-1) is a
#   multiple of D.

# Minimize x: x^2 - D y^2 = 1 for D = 2..N
def find_min_x(d):
    x = d
    while True:
        # x+1 is divisible by D: (x-1)(x+1)/D
        if is_square((x-2) * x / d):
            return x - 1
        # x-1 is divisible by D: (x-1)(x+1)/D
        elif is_square(x * (x+2) / d):
            return x + 1
        x += d

def max_minimal_diophantine(dmax):
    for d in range(2, dmax+1):
        if not is_square(d):
            print d, find_min_x(d)

# Helper functions

# Naive implementation
def is_square(n):
    return int(n ** 0.5) ** 2 == n

if __name__ == '__main__':
    BOUND = 1000
    print max_minimal_diophantine(BOUND)
