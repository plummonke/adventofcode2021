import io
import sys

from collections import Counter

def main():
    input_file = sys.argv[1]
    with io.open(input_file,"r") as f:
        input_data = f.readline().strip("\n").split(",")

    count = Counter(input_data)
    cohorts = [Cohort(y, int(x), 6) for x, y in count.items()]
    
    for day in range(256):
        new_cohorts = list(filter(lambda x: x is not None, [x.run() for x in cohorts]))
        seven_days = list(filter(lambda x: x.days == 6, cohorts))
        cohorts =  list(filter(lambda x: x.days != 6, cohorts))
        cohorts.extend(new_cohorts)
        if len(seven_days) >= 1:
            c = Cohort(0, 6, 6)
            for each in seven_days:
                c.increaseCohort(each.number)

            cohorts.append(c)

        for x in cohorts:
            print(x)

        print()

    tot = 0
    for x in cohorts:
        tot += x.number

    print(tot)

class Cohort:
    def __init__(self, num: int, days: int, reset: int):
        self.number = num
        self.days = days
        self.reset = reset

    def __str__(self):
        return f"Cohort of {self.number} lanternfish spawning in {self.days} days"

    def decrementDays(self):
        self.days -= 1

    def spawn(self):
        return Cohort(self.number, 8, 6)

    def increaseCohort(self, num):
        self.number += num

    def run(self):
        self.decrementDays()
        if self.days == -1:
            self.days = self.reset
            return self.spawn()

main()
