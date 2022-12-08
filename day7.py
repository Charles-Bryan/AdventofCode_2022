from aocd import get_data
import operator


class Node:

    def __init__(self, name, size=None, parent=None):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []
        self.is_directory = False

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self
        self.is_directory = True

    def print_node(self, prefix=''):
        print(f"{prefix}{self.name} | {self.size}")
        if self.children:
            for child_node in self.children:
                new_prefix = prefix + '-'
                child_node.print_node(new_prefix)

    def get_size(self):
        if self.size is None:
            self.calc_sizes()
        return self.size

    def calc_sizes(self):
        if self.children:
            total = 0
            for child in self.children:
                total += child.get_size()
            self.size = total

    def sizes_meeting_criteria(self, input_list, criteria, value):
        if self.is_directory & (criteria(self.size, value)):
            input_list.append(self.size)

        if self.children:
            for child in self.children:
                child.sizes_meeting_criteria(input_list, criteria, value)

    def return_node(self, child_name):
        for child in self.children:
            if child.name == child_name:
                return child


def generate_tree(input_lines):
    root = Node('root')
    current_node = root

    for line in input_lines:
        line_parts = line.split(' ')
        if line_parts[0] == '$':
            if line_parts[1] == 'ls':
                continue
            else:  # cd x or cd..
                if line_parts[2] == '..':
                    current_node = current_node.parent
                else:
                    current_node = current_node.return_node(line_parts[2])
        else:
            if line_parts[0] == 'dir':
                current_node.add_child(Node(line_parts[1]))
            else:
                current_node.add_child(Node(line_parts[1], int(line_parts[0])))
    return root


# --- Day 7: No Space Left On Device ---
# Getting the input
raw_data = get_data(day=7, year=2022)
lines = raw_data.split('\n')

# Making my tree and assigning sizes to each node
my_tree = generate_tree(input_lines=lines[1:])
my_tree.calc_sizes()

# Part 1: Sum of small directories
part1 = []
my_tree.sizes_meeting_criteria(input_list=part1, criteria=operator.le, value=100000)
print(f"Part1: {sum(part1)}")

# Part 2: Smallest directory we can remove to clear up enough space
part2 = []
available_space = 70000000 - my_tree.size
needed_space = 30000000 - available_space
my_tree.sizes_meeting_criteria(input_list=part2, criteria=operator.ge, value=needed_space)
print(f"Part2: {sorted(part2)[0]}")
