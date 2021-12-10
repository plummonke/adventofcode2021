import io
import sys

from typing import List

def main():
    input_file = sys.argv[1]
    with io.open(input_file,"r") as f:
        input_data = [x.strip("\n") for x in f]

    lines = []
    corrupted = []
    for line in input_data:
        masked = mask(line)

        if 0 in masked:
            corrupted.append(masked)
            lines.append(line)

    scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    print(score(scores, lines, corrupted))

def score(scoring: dict, orig: List[str], masked: List[List[int]]) -> int:
    score = 0
    for i, each in enumerate(masked):
        for j, x in enumerate(each):
            if x == 0:
                score += scoring[orig[i][j]]
    return score

def mask(x: str) -> List[int]:
    d = { "(": ")", "[": "]", "{": "}", "<": ">"} 
    order = []
    values = []

    for i, char in enumerate(x):
        if char in d:
            values.append(1)
            order.append(char)
        elif char == d[order[-1]]:
            values.append(-1)
            order.pop()
        else:
            values.append(0)
            order.pop()

    return values

main()
