from aocd import get_data
from collections import deque
import re
import copy

# --- Day 5: Supply Stacks ---
raw_data = get_data(day=5, year=2022)
lines = raw_data.splitlines()


def parse_input5(input):
    num_cols = (len(input[0]) + 1) // 4
    layout = []
    moves = []
    for i in range(num_cols):
        layout.append(deque(''))

    for row in input:
        if row == '':
            # Skip the blank line
            pass
        elif row[0] == 'm':
            # Parse the moves
            moves.append(list(map(int, re.findall(r'\d+', row))))
        elif row[0] == '[':
            # Parse the layout
            for i in range(num_cols):
                char = row[4*i+1]
                if char != ' ':
                    layout[i].appendleft(char)
        # else: pass

    return layout, moves


def apply_move1(layout, move_list):
    n = move_list[0]
    from_col = move_list[1]-1
    to_col = move_list[2]-1

    for _ in range(n):
        layout[to_col].append(layout[from_col].pop())


def apply_move2(layout, move_list):
    n = move_list[0]
    from_col = move_list[1]-1
    to_col = move_list[2]-1

    temp_deque = deque()
    for _ in range(n):
        temp_deque.append(layout[from_col].pop())

    for _ in range(n):
        layout[to_col].append(temp_deque.pop())


layout, moves = parse_input5(input=lines)

# Part 1: CrateMover 9000
print('Part 1')
l1 = copy.deepcopy(layout)
for move in moves:
    apply_move1(layout=l1, move_list=move)
for stack in l1:
    print(stack[-1])

# Part 2: CrateMover 9001
print('Part 2')
l2 = copy.deepcopy(layout)
for move in moves:
    apply_move2(layout=l2, move_list=move)
for stack in l2:
    print(stack[-1])
