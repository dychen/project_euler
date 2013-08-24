import sys
import curses
import random

def print_grid(ant, grid):
    pgrid = [['0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0']]
    for i, e in enumerate(grid['seeds']):
        if e == True:
            pgrid[4][i] = 'S'
    for i, e in enumerate(grid['dests']):
        if e == True:
            pgrid[0][i] = 'S'
    pgrid[ant['y']][ant['x']] = 'A'
    for col_e in pgrid:
        for row_e in col_e:
            sys.stdout.write(row_e)
        sys.stdout.write('\n')

def initialize_ant():
    ant = {}
    ant['x'] = 2
    ant['y'] = 2
    ant['has_seed'] = False
    ant['steps'] = 0
    ant['done'] = False
    return ant

def initialize_grid():
    grid = {}
    grid['seeds'] = [True] * 5
    grid['dests'] = [False] * 5
    return grid

def move(ant, grid):
    rand_array = ['N', 'S', 'E', 'W']
    x = ant['x']
    y = ant['y']
    has_seed = ant['has_seed']
    # Choose direction
    if x == 0:
        rand_array.remove('W')
    if x == 4:
        rand_array.remove('E')
    if y == 0:
        rand_array.remove('N')
    if y == 4:
        rand_array.remove('S')
    direction = random.choice(rand_array)

    # Move in that direction
    if direction == 'W':
        x -= 1
    elif direction == 'E':
        x += 1
    elif direction == 'N':
        y -= 1
    elif direction == 'S':
        y += 1

    # Pick up a seed
    if y == 4 and not has_seed:
        if grid['seeds'][x] == True:
            ant['has_seed'] = True
            grid['seeds'][x] = False

    # Drop off a seed
    if y == 0 and has_seed:
        if grid['dests'][x] == False:
            ant['has_seed'] = False
            grid['dests'][x] = True
            # Check if the ant is done
            if len(filter(lambda x: x != False, grid['dests'])) == 5:
                ant['done'] = True

    ant['steps'] += 1
    ant['x'] = x
    ant['y'] = y
    return ant, grid

def mainloop():
    ant = initialize_ant()
    grid = initialize_grid()
    while not ant['done']:
        #print_grid(ant, grid)
        ant, grid = move(ant, grid)
    num_steps = ant['steps']
    #print num_steps
    return num_steps

def run():
    sum = 0
    num_iter = 1000000
    percent = num_iter / 100
    for i in range(num_iter):
        if i % percent == 0:
            print str(float(i) / num_iter * 100) + "% done"
        sum += mainloop()
    print sum / float(num_iter)

run()