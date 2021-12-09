import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input


class PositiveList(list):

    def __getitem__(self, ind):
        if ind < 0:
            return None
        return super(PositiveList, self).__getitem__(ind)


lines = Input.get_lines(os.path.basename(__file__))

lines = PositiveList([PositiveList([int(height) for height in list(line.strip())]) for line in lines])

calls = 0


def get_lowest_point(x, y, lines, init=False):
    global calls
    if init:
        calls += 1

    point = lines[x][y]

    # if point == 0:
    #     return x, y, point

    up_x = x-1
    try:
        up = lines[up_x][y]
    except (TypeError, IndexError):
        up = None

    down_x = x+1
    try:
        down = lines[down_x][y]
    except (TypeError, IndexError):
        down = None

    left_y = y-1
    try:
        left = lines[x][left_y]
    except (TypeError, IndexError):
        left = None

    right_y = y+1
    try:
        right = lines[x][right_y]
    except (TypeError, IndexError):
        right = None

    nearest_lowest = set()

    if up is not None and up < point:
        nearest_lowest.union(get_lowest_point(up_x, y, lines))

    if down is not None and down < point:
        nearest_lowest.union(get_lowest_point(down_x, y, lines))

    if left is not None and left < point:
        nearest_lowest.union(get_lowest_point(x, left_y, lines))

    if right is not None and right < point:
        nearest_lowest.union(get_lowest_point(x, right_y, lines))

    if right == left and left == up and up == down and down == point:
        return set()

    if len(nearest_lowest) == 0:
        nl_set = set()
        nl_set.add((x, y, point))
        return nl_set
    else:
        return nearest_lowest


low_points = set()

for x, line in enumerate(lines):
    for y, height in enumerate(line):
        for point in get_lowest_point(x, y, lines, True):
            if type(point) == int:
                print(x, y, point)
            low_points.add(point)

sum_of_risk = 0
for low_point in low_points:
    risk_level = 1 + low_point[2]
    sum_of_risk += risk_level

print("Part 1:")
print(calls)
print(sum_of_risk)
