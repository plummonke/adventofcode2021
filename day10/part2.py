import io
import sys

from typing import List

def main():
    input_file = sys.argv[1]
    with io.open(input_file,"r") as f:
        input_data = [x.strip("\n") for x in f]

    lines = []
    for line in input_data:
        masked = mask(line)

        if 0 not in masked:
            lines.append(line)

    scores = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }

    completion = [evalComplete(x) for x in lines]
    scored_values = sorted([score(scores, x) for x in completion])
    print(scored_values[len(scored_values)//2])

def score(scoring: dict, ans: str) -> int:
    score = 0
    for x in ans:
        score *= 5
        score += scoring[x]
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

def evalComplete(x: str) -> str:
    d = { "(": ")", "[": "]", "{": "}", "<": ">"} 
    order = []

    for char in x:
        if char in d:
            order.append(char)
        else:
            order.pop()

    return "".join(d[x] for x in order[::-1])

main()
