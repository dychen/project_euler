def generate_triangles(n):
    triangles = []
    for m in range(1, n+1):
        triangles.append(m * (m+1) / 2)
    return set(triangles)

triangles = generate_triangles(1000)

file = open('tmp.txt', 'r')

words = []
count = 0
for line in file:
    words += map(lambda x: x[1:-1], line.strip().split(','))
for word in words:
    sum = 0
    for c in word:
        sum += (ord(c) - 64)
    if sum in triangles:
        print word + ": " + str(sum)
        count += 1
print count

file.close()