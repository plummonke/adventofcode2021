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

    result = Counter(template[i:i + 2] for i in range(len(template) - 1))
    alpha_counter = Counter(template)

    for step in range(steps):
        c = result.most_common()
        new_result = Counter()
        for each in c:
            char = instructions[each[0]]
            alpha_counter.update({char: each[1]})
            new_result.update({each[0][0] + char: each[1]})
            new_result.update({str(char) + each[0][1]: each[1]})

        result = new_result

    totals = alpha_counter.most_common()
    print(totals[0][1] - totals[-1][1])

main()
