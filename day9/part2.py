import io
import sys

from typing import List, Tuple, Set

def main():
    input_file = sys.argv[1]
    with io.open(input_file,"r") as f:
       input_data = [[int(y) for y in x.strip("\n")] for x in f.readlines()]

    basins = []
    coords_in_basin = set()
    for i, line in enumerate(input_data):
        for j, num in enumerate(line):
            if (i, j) not in coords_in_basin:
                basin = discernBasin(i, j, input_data)
                basins.append(len(basin))
                coords_in_basin.update(basin)

    answer = 1
    for num in sorted(basins)[-3:]:
        answer *= num

    print(answer)

def discernBasin(row: int, col:int, matrix: List[List[int]]) -> Set[Tuple[int,int]]:
    out = set()
    done = False

    next = [(row, col)]
    while not done:
        i, j = next.pop()
        if matrix[i][j] != 9:
            out.add((i, j))
            adjacent = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

            next.extend([each for each in adjacent 
                if 0 <= each[0] < len(matrix) 
                and 0 <= each[1] < len(matrix[i]) 
                and each not in out])

        if len(next) == 0:
            done = True

    return out

main()
