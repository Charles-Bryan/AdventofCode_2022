from aocd import get_data
from collections import defaultdict
import re
import math


def parse_input(input_lines):
    monkeys = {}
    starting_pairs = []
    i = 0
    length = len(input_lines)
    lazy_multiple = 1
    while i < length:
        num = re.findall('\d+', input_lines[i])[0]
        starting_pairs.append(re.findall('\d+', input_lines[i+1]))
        _, _, mod = input_lines[i+2].partition('= ')
        comp = re.findall('\d+', input_lines[i + 3])[0]
        t = re.findall('\d+', input_lines[i + 4])[0]
        f = re.findall('\d+', input_lines[i + 5])[0]

        lazy_multiple *= int(comp)
        monkeys[int(num)] = {'mod': '(' + mod + ')',
                             'comp': 'int(x%' + comp + '==0)*(t-f) + f',
                             't': int(t),
                             'f': int(f)}
        i += 7

    return starting_pairs, monkeys, lazy_multiple


def monkey_games(num_rounds, monkeys, starting_positions, multiple=None):
    if multiple is None:  # Part 1
        post_modifier = '//3'
    else:  # Part 2
        post_modifier = '%' + str(multiple)

    dd = defaultdict(int)

    for ix, vals in enumerate(starting_positions):
        m_num = ix
        for val in vals:
            r = 1
            while r <= num_rounds:
                dd[m_num] += 1  # Monkey does an investigation
                val = eval(monkeys[m_num]['mod'] + post_modifier, {}, {'old': int(val)})
                m_num_new = eval(monkeys[m_num]['comp'], {}, {'x': val, 't': monkeys[m_num]['t'], 'f': monkeys[m_num]['f']})
                if m_num_new <= m_num:
                    r += 1  # This item won't be investigated again until the next round
                m_num = m_num_new
            m_num = ix

    return math.prod(sorted(dd.values(), reverse=True)[0:2])


# --- Day 11: Monkey in the Middle ---
# Getting the input
raw_data = get_data(day=11, year=2022)
input_lines = raw_data.split('\n')

sp, M, lm = parse_input(input_lines=input_lines)

# Part 1: Restrained Emotions
part1 = monkey_games(num_rounds=20, monkeys=M, starting_positions=sp, multiple=None)
print(f"Part1: {part1}")

# Part 2: Limitless Worrying
part2 = monkey_games(num_rounds=10000, monkeys=M, starting_positions=sp, multiple=lm)
print(f"Part2: {part2}")
