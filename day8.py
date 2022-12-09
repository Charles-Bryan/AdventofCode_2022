# Ugly brute force approach. I think Part 1 can be done only iterating over each cell
# twice (rather than the brute force 4x), but this doesn't translate to Part 2

from aocd import get_data
import numpy as np


def process_input(split_lines):
    a = []
    for line in split_lines:
        a.append([int(x) for x in line])

    return np.array(a)


def process_row(row):
    max = -1
    bool_row = []
    for e in row:
        if e > max:
            max = e
            bool_row.append(1)
        else:
            bool_row.append(0)
    return bool_row


def process_cell_right(cell_val, input):
    total = 0
    for e in input:
        total += 1
        if e >= cell_val:
            return total
    return total


# --- Day 8: Treetop Tree House ---
# Getting the input
raw_data = get_data(day=8, year=2022)
lines = raw_data.split('\n')

# Part 1:
input_array = process_input(split_lines=lines)

directions = []
for i in range(4):
    l = []
    for row in np.rot90(input_array, k=i):
        l.append(process_row(row=row))
    directions.append(np.rot90(np.array(l), k=-i))

print(f"Part 1: {sum(sum(directions[0] | directions[1] | directions[2] | directions[3]))}")

# Part 2:
input_array = process_input(split_lines=lines)
views = []
for i in range(4):
    l = []
    for row in np.rot90(input_array, k=i):
        r = []
        for ix, cell in enumerate(row):
            if ix+1 == len(row):
                r.append(0)
            else:
                cells_right = row[ix+1:]
                r.append(process_cell_right(cell_val=cell, input=cells_right))
        l.append(r)
    views.append(np.rot90(np.array(l), k=-i))
print(f"Part 2: {(views[0] * views[1] * views[2] * views[3]).max()}")
