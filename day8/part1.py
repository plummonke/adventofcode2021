import io
import sys

from collections import Counter

def main():
    input_file = sys.argv[1]
    with io.open(input_file,"r") as f:
        input_data = [x.split("|") for x in f]

    tot = 0
    for line in input_data:
        for each in line[1].split():
            if len(each) in (2, 3, 4, 7):
                tot += 1

    print(tot)

main()
