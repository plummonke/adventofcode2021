import collections
import io
import sys

def main():
    input_file = sys.argv[1]
    with io.open(input_file,"r") as f:
        data = [line.strip("\n") for line in f]

    pivot = [[x[i] for x in data] for i in range(len(data[0]))]
    colls = [collections.Counter(x) for x in pivot]

    gamma = convertToInt("".join([x.most_common(1)[0][0] for x in colls]))
    epsilon = convertToInt("".join([x.most_common(2)[1][0] for x in colls]))

    print(gamma * epsilon)

def convertToInt(s: str) -> int:
    length = len(s)
    num = 0
    for i, char in enumerate(s):
        position = length - 1 - i
        num += int(char) * 2 ** position

    return num

main()
