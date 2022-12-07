from aocd import get_data
from collections import Counter


def all_unique(counter):
    return counter.most_common(1)[0][1] <= 1


def marker_detection(input, length):
    c = Counter(input[:length])
    if all_unique(c):
        return length
    else:
        for ix, char in enumerate(input[length:]):
            c[input[ix]] -= 1
            c[char] += 1
            if all_unique(c):
                return ix + length + 1


# --- Day 6: Tuning Trouble ---
raw_data = get_data(day=6, year=2022)

# Part 1: marker length = 4
marker_length = 4
print(f"Part 1: {marker_detection(raw_data, marker_length)}")

# Part 1: marker length = 14
marker_length = 14
print(f"Part 2: {marker_detection(raw_data, marker_length)}")
