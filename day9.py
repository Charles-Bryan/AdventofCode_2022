from aocd import get_data


class knot:
    def __init__(self, name, x=0, y=0, parent=None, child=None):
        self.name = name
        self.x = x
        self.y = y
        self.parent = parent
        self.child = child
        self.places = set()

    def add_child(self, child_node):
        self.child = child_node
        self.child.parent = self

    def update_child(self):
        if (self.parent.x-1 <= self.x <= self.parent.x+1) & (self.parent.y-1 <= self.y <= self.parent.y+1):
            # no movement necessary
            pass
        else:
            if self.parent.x > self.x:
                self.x += 1
            if self.parent.x < self.x:
                self.x -= 1
            if self.parent.y > self.y:
                self.y += 1
            if self.parent.y < self.y:
                self.y -= 1

            if self.child is not None:
                self.child.update_child()
        self.places.add((self.x, self.y))

    def update(self, move):
        dir, num = move.split(' ')
        for _ in range(int(num)):
            if dir == 'L':
                self.x = self.x-1
            elif dir == 'R':
                self.x = self.x+1
            elif dir == 'D':
                self.y = self.y-1
            else:
                self.y = self.y+1
            self.child.update_child()


# --- Day 9: Rope Bridge ---
# Getting the input
raw_data = get_data(day=9, year=2022)
input_lines = raw_data.split('\n')

# Part 1: Short Rope
# Make our rope
rope_length = 2
top_knot = knot(name='H')
bot_knot = top_knot
for i in range(1, rope_length, 1):
    new_knot = knot(name=str(i))
    bot_knot.add_child(new_knot)
    bot_knot = new_knot

# Go through the moves
for move in input_lines:
    top_knot.update(move)

print(f"Part1: {len(bot_knot.places)}")

# Part 2: Longer rope
# Make our rope
rope_length = 10
top_knot = knot(name='H')
bot_knot = top_knot
for i in range(1, rope_length, 1):
    new_knot = knot(name=str(i))
    bot_knot.add_child(new_knot)
    bot_knot = new_knot

# Go through the moves
for move in input_lines:
    top_knot.update(move)

print(f"Part2: {len(bot_knot.places)}")