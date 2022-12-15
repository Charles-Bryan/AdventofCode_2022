from aocd import get_data
import re


def straight_line_given_ends(point1: tuple, point2: tuple) -> list:
   # Includes end points
    points = []
    x1, y1 = int(point1[0]), int(point1[1])
    x2, y2 = int(point2[0]), int(point2[1])

    if x1 == x2:
        if y1 > y2:
            points.extend([(x1, a) for a in list(range(y2, y1 + 1, 1))])
        else:
            points.extend([(x1, a) for a in list(range(y1, y2 + 1, 1))])
    else:
        if x1 > x2:
            points.extend([(a, y1) for a in list(range(x2, x1 + 1, 1))])
        else:
            points.extend([(a, y1) for a in list(range(x1, x2 + 1, 1))])

    return points


def next_cell(cur_cell: tuple, rocks: set) -> tuple:

    if (cur_cell[0], cur_cell[1]+1) not in rocks:
        return (cur_cell[0], cur_cell[1]+1)
        # check down left
    elif (cur_cell[0]-1, cur_cell[1] + 1) not in rocks:
        return (cur_cell[0]-1, cur_cell[1] + 1)
        # check down right
    elif (cur_cell[0] + 1, cur_cell[1] + 1) not in rocks:
        return (cur_cell[0] + 1, cur_cell[1] + 1)
    else:
        return cur_cell


# --- Day 14: Regolith Reservoir ---
# Getting the input
raw_data = get_data(day=14, year=2022)
input_lines = raw_data.split('\n')

rocks = set()
for row in input_lines:
    corners = re.findall('(\d+),(\d+)', row)
    for ix in range(len(corners)-1):
        line_points = straight_line_given_ends(corners[ix], corners[ix+1])
        rocks.update(line_points)

max_y = max([y for x, y in rocks])

start_cell = (500, 0)
cur_cell = start_cell

sand_stuck = 0
rocks_collecting = True
while rocks_collecting:
    next_c = next_cell(cur_cell, rocks)
    if (cur_cell == next_c) or (cur_cell[1] == max_y + 1):
        sand_stuck += 1
        if cur_cell == start_cell:
            rocks_collecting = False
        rocks.add(cur_cell)
        cur_cell = start_cell
    # elif next_c[1] >= max_y:
    #     rocks_collecting = False
    else:
        cur_cell = next_c

print(sand_stuck)
