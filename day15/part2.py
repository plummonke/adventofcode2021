import io
import math
import sys

from typing import List

def main():
    input_file = sys.argv[1]
    with io.open(input_file,"r") as f:
        input_data = [x.strip("\n") for x in f]

    matrix = expand([[int(num) for num in line] for line in input_data], 4)

    destination = (len(matrix[0]) - 1, len(matrix) - 1)
    print(scan(destination, matrix))

def scan(dest: tuple[int,int], matrix: List[List[int]]) -> List[tuple[int,int]]:
    if dest[0] >= len(matrix[0]) or dest[1] >= len(matrix):
        raise IndexError("Traveller: Destination outside of provided matrix.")

    lenx = len(matrix[0])
    leny = len(matrix)

    tentative = [[math.inf for x in range(lenx)] for y in range(leny)]
    tentative[0][0] = 0
    queue = [(0, 0)]

    while len(queue) > 0:
        i, j = queue.pop(0)
        adj = [
            (i + x, j + y) 
            for x in range(-1, 2)
            for y in range(-1, 2)
            if 0 <= i + x < lenx and 0 <= j + y < leny
            and (x != 0 or y != 0)
            and x != y and x != -y
        ]
        for x, y in adj:
            total = tentative[i][j] + matrix[x][y]
            if total < tentative[x][y]:
                tentative[x][y] = total
                queue.append((x, y))

    return tentative[dest[0]][dest[1]]

def expand(matrix: List[List[int]], times: int) -> List[List[int]]:
    temp = []
    
    for row in matrix:
        new_row = [*row]
        for i in range(times):
            new_row.extend(increment_list(row, i + 1))
        temp.append(new_row)

    out = [x for x in temp]

    for i in range(times):
        for row in temp:
            out.append(increment_list(row, i + 1))

    return out

def increment_list(arr: List[int], inc: int) -> List[int]:
    return [x + inc if x + inc <= 9 else x + inc - 9 for x in arr]

main()
