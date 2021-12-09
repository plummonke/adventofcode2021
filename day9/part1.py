import io
import sys

def main():
    input_file = sys.argv[1]
    with io.open(input_file,"r") as f:
       input_data = [[int(y) for y in x.strip("\n")] for x in f.readlines()]

    lowest = []
    for i, line in enumerate(input_data):
        for j, num in enumerate(line):
            if num == 9:
                continue

            adjacent = [num + 1] * 4
            if i != 0:
                adjacent[0] = input_data[i - 1][j]

            if i != len(input_data) - 1:
                adjacent[1] = input_data[i + 1][j]

            if j != 0:
                adjacent[2] = input_data[i][j - 1]

            if j != len(line) - 1:
                adjacent[3] = input_data[i][j + 1]

            if num < min(adjacent):
                lowest.append(num)

    print(sum(lowest) + len(lowest))

main()
