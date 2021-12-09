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


def get_lowest_point(x, y):
    point = lines[x][y]

    up_x = x-1
    try:
        up = lines[up_x][y]
    except IndexError:
        up = None

    down_x = x+1
    try:
        down = lines[down_x][y]
    except IndexError:
        down = None

    left_y = x-1
    try:
        left = lines[x][left_y]
    except IndexError:
        left = None

    right_y = x+1
    try:
        right = lines[x][right_y]
    except IndexError:
        right = None

    if up and up < point:
        return get_lowest_point(up_x, y)

    if down and down < point:
        return get_lowest_point(down_x, y)

    if left and left < point:
        return get_lowest_point(x, left_y)

    if right and right < point:
        return get_lowest_point(x, right_y)

    return x, y


low_points = set()

for x, line in enumerate(lines):
    for y, height in enumerate(line):
        low_points.add(get_lowest_point(x, y))

print(low_points)
pass
