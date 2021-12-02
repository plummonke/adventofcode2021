import io
import sys

def main():
    input_file = sys.argv[1]
    with io.open(input_file,"r") as f:
        directions = [line.split(" ") for line in f]

    sub = Submarine()
    mapping = {
        "forward": sub.forward,
        "up": sub.up,
        "down": sub.down
    }

    for direction, amount in directions:
        mapping[direction](int(amount))

    print(sub.x * sub.y)

class Submarine:
    def __init__(self):
        self.x = 0
        self.y = 0

    def forward(self, distance):
        self.x += distance

    def down(self, depth):
        self._change_depth(depth)

    def up(self, depth):
        self._change_depth(-1 * depth)

    def _change_depth(self, change):
        self.y += change

main()
