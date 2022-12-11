from aocd import get_data


def append_char(string, position, value):
    if value-1 <= position % 40 <= value+1:
        return string + '#'
    else:
        return string + '.'


# --- Day 10: Cathode-Ray Tube ---
# Getting the input
raw_data = get_data(day=10, year=2022)
input_lines = raw_data.split('\n')

# Looping through the instructions
cycle_values = []
cur_val = 1
output = 0
ix = 1
string_thing = append_char(string='', position=ix-1, value=cur_val)
for line in input_lines:
    if line == 'noop':
        ix += 1
    else:
        ix += 1
        string_thing = append_char(string=string_thing, position=ix-1, value=cur_val)
        if ix % 40 == 20:
            output += ix*cur_val
        ix += 1
        cur_val += int(line.split(' ')[1])
    string_thing = append_char(string=string_thing, position=ix-1, value=cur_val)
    if ix % 40 == 20:
        output += ix * cur_val

print(f"Part1: {output}")

crt_length = 40
lines = [string_thing[i*crt_length:crt_length*(i+1)] + '\n' for i in range(0, len(string_thing)//crt_length)]
print(f"Part2:")
print(''.join(lines))