import io
import sys

from collections import Counter

def main():
    input_file = sys.argv[1]
    with io.open(input_file,"r") as f:
        input_data = [x.split("|") for x in f]

    digits = {"abcefg": "0", "cf": "1", "acdeg": "2", "acdfg": "3", "bcdf": "4", "abdfg": "5", "abdefg": "6", "acf": "7", "abcdefg": "8", "abcdfg": "9"}

    numbers = []
    for line in input_data:
        counts = Counter(line[0].replace(" ",""))
        trans = {x[0]: {4:"e",6:"b",9:"f"}[x[1]]for x in counts.items() if x[1] in (4,6,9)}

        for each in line[0].split():
            if len(each) == 2:
                trans.update({seg: "c" for seg in each if seg not in trans})
        
        trans.update({x[0]: "a" for x in counts.items() if x[1] == 8 and x[0] not in trans})

        for each in line[0].split():
            if len(each) == 4:
                trans.update({seg: "d" for seg in each if seg not in trans})

        trans.update({x[0]: "g" for x in counts.items() if x[1] == 7 and x[0] not in trans})
        deciphered = line[1].translate(str.maketrans(trans)).split()

        numbers.append(int("".join([digits["".join(sorted(term))] for term in deciphered])))

    print(sum(numbers))

main()
