import os
import sys
import itertools

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input

lines = Input.get_lines(os.path.basename(__file__))

fishes = [int(fish) for fish in lines[0].split(",")]

days = 256

while days != 0:
    new_fishes = 0
    for id, fish in enumerate(fishes):
        if fish == 0:
            fishes[id] = 6
            new_fishes += 1
        else:
            fishes[id] -= 1
    for _ in itertools.repeat(None, new_fishes):
        fishes.append(8)
    days -= 1
    print(days)

print(len(fishes))
