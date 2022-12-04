# Community accepted safe way of retrieving and caching the data without stressing the AoC servers
from aocd import get_data

# --- Day 3: Rucksack Reorganization ---
# Get the data
raw_data = get_data(day=3, year=2022)
lines = raw_data.splitlines()


def sum_chars(input):
    total = 0
    for char in input:
        if ord(char) < 91:
            total += ord(char) - 38
        else:
            total += ord(char) - 96

    return total


def char_in_all(s_list):
    for char in s_list[0]:
        found = True
        for s in s_list[1:]:
            if char not in s:
                found = False
                break
        if found:
            return char


def input_split(input, method):
    if method == 'part1':
        return [[s[:len(s) // 2], s[len(s) // 2:]] for s in input]
    if method == 'part2':
        return [lines[3*i:3*(i+1)] for i in range(len(lines)//3)]


# Part 1: matching character in front and back
parsed_input = input_split(input=lines, method='part1')
chars = [char_in_all(strings) for strings in parsed_input]
print(sum_chars(chars))

# Part 2: Matching character across 3 Elves
parsed_input = input_split(input=lines, method='part2')
chars = [char_in_all(strings) for strings in parsed_input]
print(sum_chars(chars))
