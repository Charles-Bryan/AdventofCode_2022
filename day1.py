# Community accepted safe way of retrieving and caching the data without stressing the AoC servers
from aocd import get_data

# --- Day 1: Calorie Counting ---
# Get the data
raw_data = get_data(day=1, year=2022)
lines = raw_data.splitlines()
# Add a blank at the end to make the looping function easier
lines.append('')


def topn_elf_calories(input, n):
    elf_calories = []
    total = 0
    for snack in input:
        if snack == '':
            elf_calories.append(total)
            total = 0
        else:
            total += int(snack)

    elf_calories.sort(reverse=True)
    return sum(elf_calories[:n])


# Part 1: The most calories held by any individual elf
print(topn_elf_calories(input=lines, n=1))

# Part 2: The sum of calories held by the 3 elfs with the most calories
print(topn_elf_calories(input=lines, n=3))