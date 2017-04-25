"""
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

def find_right_triangles(p):
    right_triangles = []
    for a in range(1, p):
        rem = p - a
        for b in range(a, rem):
            c = rem - b
            if (a ** 2 + b ** 2 == c ** 2):
                right_triangles.append((a, b, c))
    return right_triangles

def find_max_right_triangles(perimeter=1000):
    return max([(p, len(find_right_triangles(p))) for p in range(1, perimeter+1)],
               key=lambda x: x[1])

print find_max_right_triangles()

