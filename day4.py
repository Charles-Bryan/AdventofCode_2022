# Community accepted safe way of retrieving and caching the data without stressing the AoC servers
from aocd import get_data
import re
# --- Day 4: Camp Cleanup ---
# Get the data
raw_data = get_data(day=4, year=2022)
lines = raw_data.splitlines()


# Part 1: Number of fully contained pairs
split_lines = [re.split(',|-', line) for line in lines]
total = 0
for pair in split_lines:
    if int(pair[0]) >= int(pair[2]) and int(pair[1]) <= int(pair[3]):
        total += 1
    elif int(pair[2]) >= int(pair[0]) and int(pair[3]) <= int(pair[1]):
        total += 1
print(total)

# Part 2: Number of overlapping pairs
split_lines = [re.split(',|-', line) for line in lines]
total = 0
for pair in split_lines:
    if int(pair[0]) <= int(pair[2]) and int(pair[1]) >= int(pair[2]):
        total += 1
    elif int(pair[2]) <= int(pair[0]) and int(pair[3]) >= int(pair[0]):
        total += 1
print(total)
