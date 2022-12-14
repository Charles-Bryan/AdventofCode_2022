from aocd import get_data


def compare(left, right):
    # Both int
    if (type(left) == int) and (type(right) == int):
        if left < right:
            return True
        elif right < left:
            return False
        else:
            pass

    # List, int
    elif (type(left) == list) and (type(right) == int):
        return compare(left, [right])

    # int, list
    elif (type(left) == int) and (type(right) == list):
        return compare([left], right)

    else:  # Both are list
        for l, r in zip(left, right):
            result = compare(l, r)
            if result == None:
                continue
            elif result == True:
                return True
            elif result == False:
                return False
        if len(left) < len(right):
            return True
        elif len(left) > len(right):
            return False


# --- Day 13: Distress Signal ---
# Getting the input
raw_data = get_data(day=13, year=2022)
input_lines = raw_data.split('\n')

# Both Parts
num_pairs = int(len(input_lines)/3)

index1 = 1
index2 = 2
list1 = [[2]]
list2 = [[6]]

total = 0
for i in range(1, num_pairs+2):
    line1 = eval(input_lines[3*(i-1)])
    line2 = eval(input_lines[3 * (i - 1) + 1])

    # Part 1 comparisons
    if compare(line1, line2):
        total += i

    # Part 2 comparisons
    if compare(line1, list1):
        index1 += 1
    if compare(line2, list1):
        index1 += 1
    if compare(line1, list2):
        index2 += 1
    if compare(line2, list2):
        index2 += 1

print(f"Part1: {total}")
print(f"Part2: {index1*index2}")
