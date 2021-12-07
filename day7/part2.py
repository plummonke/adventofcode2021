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
    mean = int(stats.mean(input_data))
    tenth = len(input_data) // 10

    costs = []
    for target in range(mean - tenth, mean + tenth + 1):
        print(target)
        costs.append(sum([moveCost(int(math.fabs(x[0] - target))) * x[1] for x in positions]))

    print(min(costs))

def moveCost(x: int):
    return sum(num for num in range(1, x + 1))

main()
