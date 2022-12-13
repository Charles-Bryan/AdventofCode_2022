from aocd import get_data
import numpy as np


def return_height(letter):
    if letter == 'S':
        return ord('a')
    elif letter == 'E':
        return ord('z')
    else:
        return ord(letter)

def return_cell_height(grid, cell):
    return grid.heights[cell[1], cell[0]]

def return_cell_path(grid, cell):
    return grid.path_lengths[cell[1], cell[0]]

def get_valid_neighbors(grid, cell):
    cur_x = cell[0]
    cur_y = cell[1]
    cur_height = return_cell_height(grid, cell)

    valid_neighbors = []
    if cur_y >= 1:  # Up
        new_height = return_cell_height(grid, (cur_x, cur_y-1))
        if eval(grid.criteria, {}, {'cur_h': cur_height, 'new_h': new_height}):
            valid_neighbors.append((cur_x, cur_y - 1))

    if cur_x + 2 <= grid.grid_x:  # Right
        new_height = return_cell_height(grid, (cur_x + 1, cur_y))
        if eval(grid.criteria, {}, {'cur_h': cur_height, 'new_h': new_height}):
            valid_neighbors.append((cur_x + 1, cur_y))

    if cur_y + 2 <= grid.grid_y:  # Down
        new_height = return_cell_height(grid, (cur_x, cur_y + 1))
        if eval(grid.criteria, {}, {'cur_h': cur_height, 'new_h': new_height}):
            valid_neighbors.append((cur_x, cur_y + 1))

    if cur_x >= 1:  # Left
        new_height = return_cell_height(grid, (cur_x - 1, cur_y))
        if eval(grid.criteria, {}, {'cur_h': cur_height, 'new_h': new_height}):
            valid_neighbors.append((cur_x - 1, cur_y))

    return valid_neighbors

class Grid:
    def __init__(self, text_lines, eligibility_criteria):
        self.criteria = eligibility_criteria

        letter_array = []
        for line in text_lines:
            letter_array.append([char for char in line])
        self.letter_grid = np.array(letter_array)

        self.heights = np.vectorize(return_height)(letter_array)

        self.path_lengths = np.full(self.heights.shape, 999_999)
        self.path_lengths[np.where(self.letter_grid == 'E')] = 0

        self.grid_y, self.grid_x = self.letter_grid.shape


# --- Day 12: Hill Climbing Algorithm ---
# Getting the input
raw_data = get_data(day=12, year=2022)
input_lines = raw_data.split('\n')

# Part 0: "Traversing" the grid
my_grid = Grid(text_lines=input_lines, eligibility_criteria='cur_h <= new_h + 1')

changed_list = np.where(my_grid.path_lengths == 0)
changed_cells = [(x, y) for y, x in zip(changed_list[0], changed_list[1])]

while len(changed_cells) > 0:
    new_changed_cells = set()
    for cell in changed_cells:
        cur_path = return_cell_path(my_grid, cell)
        valid_neighbors = get_valid_neighbors(grid=my_grid, cell=cell)
        for neighbor in valid_neighbors:
            neighbor_path = return_cell_path(my_grid, neighbor)
            if cur_path + 1 < neighbor_path:
                my_grid.path_lengths[neighbor[1], neighbor[0]] = cur_path + 1
                new_changed_cells.add(neighbor)
    changed_cells = new_changed_cells

# Part 1
print(f"Part1: {my_grid.path_lengths[my_grid.letter_grid == 'S'][0]}")

# Part 2:
print(f"Part1: {my_grid.path_lengths[my_grid.heights == ord('a')].min()}")
