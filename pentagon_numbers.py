import sys

def generate_pentagonal(maximum):
    pent = []
    for n in range(1, maximum+1):
        pent.append(n * (3*n-1) / 2)
    return pent

NUM_MAX = 10000
pent_list = generate_pentagonal(NUM_MAX)
pent_set = set(pent_list[:])
min_dif = sys.maxint
print pent_list
print pent_set
for i in range(len(pent_list)):
    for j in range(i+1, len(pent_list)):
        sum = pent_list[j] + pent_list[i]
        dif = pent_list[j] - pent_list[i]
        if sum in pent_set and dif in pent_set and dif < min_dif:
            print pent_list[i], pent_list[j]
            min_dif = dif
print min_dif