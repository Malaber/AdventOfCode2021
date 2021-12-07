import os
import sys
import itertools

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input

lines = Input.get_lines(os.path.basename(__file__))

fishes = [int(fish) for fish in lines[0].split(",")]

fishes_compact = {}
possible_values = range(0, 9)
for i in possible_values:
    fishes_compact[i]=fishes.count(i)

print(fishes_compact)

final_day = 256
day = 0


def print_fishes(day, fishes):
    print(f"Day {day}: {sum(fishes.values())}")


while day != final_day:
    new_fishes = {}
    for k,v in fishes_compact.items():
        new_fishes[k-1] = v
    new_fishes[8] = new_fishes[-1]
    new_fishes[6] += new_fishes[-1]
    del new_fishes[-1]

    fishes_compact = new_fishes

    day += 1
    #print(day)
    if day == 80:
        print("Part 1")
        print_fishes(day, fishes_compact)

print("Part 2")
print_fishes(final_day, fishes_compact)
