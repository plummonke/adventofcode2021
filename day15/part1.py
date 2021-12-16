import io
import math
import sys

from typing import List

def main():
    input_file = sys.argv[1]
    with io.open(input_file,"r") as f:
        input_data = [x.strip("\n") for x in f]

    matrix = [[int(num) for num in line] for line in input_data]

    destination = (len(matrix[0]) - 1, len(matrix) - 1)
    print(scan(destination, matrix))

def scan(dest: tuple[int,int], matrix: List[List[int]]) -> List[tuple[int,int]]:
    if dest[0] >= len(matrix[0]) or dest[1] >= len(matrix):
        raise IndexError("Traveller: Destination outside of provided matrix.")

    lenx = len(matrix[0])
    leny = len(matrix)

    visited = set()
    unvisited = {(x, y) for x in range(lenx) for y in range(leny)}
    tentative = [[math.inf for x in range(lenx)] for y in range(leny)]

    tentative[0][0] = 0

    for i in range(lenx):
        for j in range(leny):
            adj = [
                (i + x, j + y) 
                for x in range(-1, 2)
                for y in range(-1, 2)
                if 0 <= i + x < lenx and 0 <= j + y < leny
                and (i + x, j + y) not in visited
                and (x != 0 or y != 0)
                and x != y and x != -y
            ]
            for x, y in adj:
                total = tentative[i][j] + matrix[x][y]
                if  total < tentative[x][y]:
                    tentative[x][y] = total

            unvisited.remove((i, j))
            visited.add((i, j))

    return tentative[dest[0]][dest[1]]

main()
