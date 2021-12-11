import io
import sys

from typing import List, Tuple

def main():
    input_file = sys.argv[1]
    with io.open(input_file,"r") as f:
        input_data = [x.strip("\n") for x in f]

    matrix = [[Flasher(int(x),1,0) for x in line] for line in input_data]

    try:
        steps = int(sys.argv[2])
    except IndexError:
        steps = 0
        print("Steps value not provided")

    flashes = 0
    for _ in range(steps):
        flashed = set()
        done = False

        next = [(x, y) for x in range(len(matrix)) for y in range(len(matrix[0]))]
        while not done:
            x, y = next.pop()
            matrix[x][y].increment()

            if matrix[x][y] > 9 and (x, y) not in flashed:
                flashed.add((x, y))
                next.extend(findAdjacent(x, y, matrix))

            if len(next) == 0:
                done = True

        for x, y in flashed:
            matrix[x][y].resetFlasher()

        flashes += len(flashed)

    print(flashes)

class Flasher:
    def __init__(self, value: int, inc: int, reset: int):
        self.value = value
        self.inc = inc
        self.reset = reset

    def __str__(self):
        return f"Flasher: {self.value} + {self.inc}, reset: {self.reset}"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other: int):
        if type(other) in (int, float):
            self.value += other

        if type(other) == Flasher:
            self.value += other.value

    def __radd__(self, other):
        self.__add__(other)

    def __iadd__(self, other):
        self.__add__(other)

    def __eq__(self, other):
        if type(other) in (int, float):
            x = other
        elif type(other) == Flasher:
            x = other.value
        else:
            raise TypeError(f"Flasher cannot be compared to {type(other)}.")

        return self.value == x

    def __ne__(self, other):
        if type(other) in (int, float):
            x = other
        elif type(other) == Flasher:
            x = other.value
        else:
            raise TypeError(f"Flasher cannot be compared to {type(other)}.")

        return self.value != x

    def __lt__(self, other):
        if type(other) in (int, float):
            x = other
        elif type(other) == Flasher:
            x = other.value
        else:
            raise TypeError(f"Flasher cannot be compared to {type(other)}.")

        return self.value < x

    def __gt__(self, other):
        if type(other) in (int, float):
            x = other
        elif type(other) == Flasher:
            x = other.value
        else:
            raise TypeError(f"Flasher cannot be compared to {type(other)}.")

        return self.value > x

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def resetFlasher(self):
        self.value = self.reset

    def increment(self):
        self.value += self.inc

def findAdjacent(i: int, j: int, matrix: List[List[Flasher]]) -> set[Tuple[int, int]]:
    return filter(
        lambda x: 0 <= x[0] < len(matrix) and 0 <= x[1] < len(matrix[i]),
        [(i + x, j + y) for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0]
    )

main()
