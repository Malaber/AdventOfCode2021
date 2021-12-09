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


def get_lowest_point(x, y, lines):
    point = lines[x][y]

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

    if up is not None and up < point:
        return get_lowest_point(up_x, y, lines)

    if down is not None and down < point:
        return get_lowest_point(down_x, y, lines)

    if left is not None and left < point:
        return get_lowest_point(x, left_y, lines)

    if right is not None and right < point:
        return get_lowest_point(x, right_y, lines)

    return x, y, point


low_points = set()

for x, line in enumerate(lines):
    for y, height in enumerate(line):
        low_points.add(get_lowest_point(x, y, lines))

sum_of_risk = 0
for point in low_points:
    risk_level = 1 + point[2]
    sum_of_risk += risk_level

print("Part 1:")
print(sum_of_risk)
