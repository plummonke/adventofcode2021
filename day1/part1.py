import io
import sys

def main():
    input_file = sys.argv[1]

    with io.open(input_file,"r") as f:
        data = [int(line) for line in f]

    diffs = mapDiff(data)
    print(sum([1 for x in filter(lambda x: x > 0, diffs)]))

def mapDiff(iter):
    out = []
    for i, x in enumerate(iter):
        if i == 0:
            out.append(0)
            continue

        out.append(diff(iter[i-1], x))

    return out

def diff(a, b):
    return b - a

main()
