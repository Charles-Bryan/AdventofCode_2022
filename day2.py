# Community accepted safe way of retrieving and caching the data without stressing the AoC servers
from aocd import get_data

# --- Day 2: Rock Paper Scissors ---
# Get the data
raw_data = get_data(day=2, year=2022)
lines = raw_data.splitlines()


def tournament_sum(input, mapping):
    return(sum([mapping[round] for round in input]))


# Part 1: Misunderstanding the code
remap1 = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6,
}
print(tournament_sum(input=lines, mapping=remap1))

# Part 2: Correctly understanding the code
remap2 = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7,
}
print(tournament_sum(input=lines, mapping=remap2))