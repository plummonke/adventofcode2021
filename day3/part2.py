import collections
import io
import sys

def main():
    input_file = sys.argv[1]
    with io.open(input_file,"r") as f:
        data = [line.strip("\n") for line in f]

    oxygen = convertToInt(filterBits(data, "1"))
    co2 = convertToInt(filterBits(data, "0"))

    print(oxygen * co2)

def filterBits(data: list, default: str) -> str:
    filtered = data
    for i in range(len(data[0])):
        coll = collections.Counter([x[i] for x in filtered])
        target = default
        commons = coll.most_common()

        if commons[0][1] != commons[1][1]:
            target = commons[(1,0)[int(default)]][0]
        
        filtered = [x for x in filtered if x[i] == target]

        if len(filtered) == 1: return filtered[0]

    return "0" * len(coll)

def convertToInt(s: str) -> int:
    length = len(s)
    num = 0
    for i, char in enumerate(s):
        position = length - 1 - i
        num += int(char) * 2 ** position

    return num

main()
