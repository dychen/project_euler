def generate_triangular(maximum):
    triangles = []
    for n in range(1, maximum+1):
        triangles.append(n * (n+1) / 2)
    return triangles

def generate_pentagonal(maximum):
    pentagons = []
    for n in range(1, maximum+1):
        pentagons.append(n * (3*n-1) / 2)
    return pentagons

def generate_hexagonal(maximum):
    hexagons = []
    for n in range(1, maximum+1):
        hexagons.append(n * (2*n-1))
    return hexagons

NUM_MEMBERS = 100000
triangles = set(generate_triangular(NUM_MEMBERS))
pentagons = set(generate_pentagonal(NUM_MEMBERS))
hexagons = set(generate_hexagonal(NUM_MEMBERS))

common = triangles.intersection(pentagons)
common = common.intersection(hexagons)

print common