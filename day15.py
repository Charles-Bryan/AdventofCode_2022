from aocd import get_data
import re
from collections import Counter


def calc_dist(s, b):
    return abs(s[0] - b[0]) + abs(s[1] - b[1])


def return_no_go_cells_part1(s, b, y):
    d = calc_dist(s, b)
    temp = abs(s[1] - y)
    temp2 = d-temp
    return [x for x in range(s[0] - temp2, s[0] + temp2 + 1) if (x, y) != b]


def update_grid(x_array, y_array, s, b):
    d = calc_dist(s, b)
    for y in range(s[1] - d, s[1] + d + 1):
        if (y >= 0) and (y <= 4_000_000):
            for x in range(s[0] - d + abs(y-s[1]), s[0] + d - abs(y-s[1]) + 1):
                if (x >= 0) and (x <= 4_000_000):
                    x_array[x] += 1
                    y_array[y] += 1


def get_perimeter(s, b, bounds):
    d = calc_dist(s, b)
    cells = set()
    for y in range(s[1] - d - 1, s[1] + d + 2):
        if (y >= bounds[0]) and (y <= bounds[1]):
            remaining_distance = (d+1) - abs(y-s[1])

            left_x = s[0] - remaining_distance
            if (left_x >= bounds[0]) and (left_x <= bounds[1]):
                cells.add((left_x, y))

            right_x = s[0] + remaining_distance
            if (right_x >= bounds[0]) and (right_x <= bounds[1]):
                cells.add((right_x, y))

    return cells


def cell_in_range(s, b, cell):
    return calc_dist(s, cell) <= calc_dist(s, b)


# --- Day 15: Beacon Exclusion Zone ---
# Getting the input
raw_data = get_data(day=15, year=2022)
input_lines = raw_data.split('\n')

s_and_b = []
for line in input_lines:
    sensor, beacon = re.findall('x=(-?\d+), y=(-?\d+)', line)
    sensor = (int(sensor[0]), int(sensor[1]))
    beacon = (int(beacon[0]), int(beacon[1]))
    s_and_b.append((sensor, beacon))

key_height = 2000000
no_go_cells = set()

bounds = (0, 4000000)
perimeter_cells = Counter()
for sensor, beacon in s_and_b:
    l = return_no_go_cells_part1(sensor, beacon, key_height)
    no_go_cells.update(l)

    cells = get_perimeter(sensor, beacon, bounds)
    perimeter_cells.update(cells)
print(f"Part1: {len(no_go_cells)}")

# Part 2
reduced_perimeter_cells = [cell for cell in perimeter_cells if perimeter_cells[cell] > 1]
for cell in reduced_perimeter_cells:
    detected_cell = False
    for sensor, beacon in s_and_b:
        if cell_in_range(sensor, beacon, cell):
            detected_cell = True
            break
    if not detected_cell:
        print(f"Part2: {cell[0]*4000000+cell[1]}")
        break
