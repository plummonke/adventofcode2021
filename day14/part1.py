import io
import sys

from collections import Counter

def main():
    input_file = sys.argv[1]

    try:
        steps = int(sys.argv[2])
    except IndexError as e:
        print(e)
        print("Error: Steps not provided.")
        exit(1)

    with io.open(input_file,"r") as f:
        input_data = [x.strip("\n") for x in f]

    template = input_data[0]
    instructions = {x[0]: x[1] for x in [line.split(" -> ") for line in input_data[2:]]}

    result = template
    for step in range(steps):
        new_str = result[0]
        for i, _ in enumerate(result[:-1]):
            new_str += insert_between(result[i+1], instructions[result[i:i+2]])

        result = new_str

    count = Counter(result)
    totals = count.most_common()
    print(totals[0][1] - totals[-1][1])

def insert_between(char: str, insert: str) -> str:
    return insert + char

main()
