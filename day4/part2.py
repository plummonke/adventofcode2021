import io
import re
import sys

def main():
    input_file = sys.argv[1]
    with io.open(input_file,"r") as f:
        input_data = [line.split("\n")[0] for line in f]

    called_numbers = input_data[0].split(",")
    boards = []
    val_dict = BingoNumbers()

    chunked = [input_data[x:x+5] for x in range(2,len(input_data),6)]
    for each in chunked:
        matrix = []
        for row in each:
            matches = re.findall('\d+', row)
            matrix.append(matches)
            val_dict.addValues(matches)

        boards.append(BingoBoard(matrix))

    for num in called_numbers:
        val_dict.markValue(num)

    filtered_boards = [x for x in filter(lambda x: x.checkBoard(val_dict) == True, boards)]
    for number in called_numbers[::-1]:
        val_dict.unmarkValue(number)
        filtered_boards2 = [x for x in filter(lambda x: x.checkBoard(val_dict) == False, filtered_boards)]
        if len(filtered_boards2) > 0:
            val_dict.markValue(number)
            print(sumBoard(filtered_boards2[0], val_dict) * int(number))
            break

class BingoNumbers(dict):
    def __init__(self):
        self.values = dict()

    def addValues(self, values: list):
        for number in values:
            self.addValue(number)

    def addValue(self, value: str):
        if value not in self:
            self[value] = False

    def markValue(self, value):
        if value in self:
            self[value] = True

    def unmarkValue(self, value):
        if value in self:
            self[value] = False

class BingoBoard:
    def __init__(self, matrix: list):
        self.matrix = matrix

    def __str__(self):
        return "\n".join([",".join(x) for x in self.matrix])

    def checkBoard(self, valuesDict) -> bool:
        return any([self._checkRows(valuesDict), self._checkColumns(valuesDict)])

    def _checkRows(self, valuesDict) -> bool:
        rows = [[valuesDict[x] for x in self.matrix[i]] for i in range(len(self.matrix))]
        return any(map(all, rows))

    def _checkColumns(self, valuesDict) -> bool:
        rows = [[valuesDict[x[i]] for x in self.matrix] for i in range(len(self.matrix))]
        return any(map(all, rows))

def sumBoard(board: BingoBoard, value_dict: dict) -> int:
    return sum([int(y) for x in board.matrix for y in x if not value_dict[y]])

main()
