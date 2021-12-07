import io
import math
import statistics as stats
import sys

from collections import Counter

def main():
    input_file = sys.argv[1]
    with io.open(input_file,"r") as f:
        input_data = [int(x) for x in f.readline().strip("\n").split(",")]

    positions = Counter(input_data).most_common()
    median = int(stats.median(input_data))

    print(sum([math.fabs(x[0] - median) * x[1] for x in positions]))

main()
