import io
import math
import sys

from typing import List

def main():
    input_file = sys.argv[1]
    with io.open(input_file,"r") as f:
        input_data = [line.strip("\n").split(" -> ") for line in f]

    lines = [Line(Point(*x.split(",")), Point(*y.split(","))) for x, y in input_data]

    plane = Plane()
    for line in lines:
        plane.addLine(line)

    total = 0
    print(plane.coordinates)
    for x in plane.coordinates:
        for y in plane.coordinates[x]:
            if plane.coordinates[x][y] >= 2:
                total += 1

    print(total)

class Point:
    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def __str__(self):
        return f"Line: {self.start} -> {self.end}"

    def __repr__(self):
        return self.__str__()

    def overlap(self, other):
        pass

    def slope(self):
        xdiff = self.start.x - self.end.x
        ydiff = self.start.y - self.end.y

        run = 1
        rise = 1

        try:
            if self.start.x != self.end.x:
                run = int(xdiff/ydiff)
            if (self.end.x < self.start.x and 0 < run) or (self.start.x < self.end.x and run < 0):
                 run *= -1
        except ZeroDivisionError:
            rise = 0

        try:
            if self.start.y != self.end.y:
                rise = int(ydiff/xdiff)
            if (self.end.y < self.start.y and 0 < rise) or (self.start.y < self.end.y and rise < 0):
                rise *= -1
        except ZeroDivisionError:
            run = 0

        return {"x":run,"y":rise}

    def interpolate(self) -> List[Point]:
        slope = self.slope()

        if slope["x"] == 0:
            ystart = min(self.start.y, self.end.y)
            yend = max(self.start.y, self.end.y) + 1
            yaxis = [y for y in range(ystart, yend)]
            return [Point(self.start.x, y) for y in yaxis]
        
        xstart = min(self.start.x, self.end.x)
        xend = max(self.start.x, self.end.x) + 1
        if slope["y"] == 0:
            xaxis = [x for x in range(xstart, xend)]
            return [Point(x, self.start.y) for x in xaxis]

        xaxis = [x for x in range(self.start.x, self.end.x + (1 * slope["x"]), slope["x"])]
        yaxis = [y for y in range(self.start.y, self.end.y + (1 * slope["y"]), slope["y"])]
        points = [Point(x, y) for x, y in zip(xaxis,yaxis)]
        
        return points

class Plane:
    def __init__(self):
        """
        Store coordinates in a nested dict. The first level of the dict is the x axis and the second is the y axis.
        """
        self.coordinates = dict()

    def addPoint(self, point: Point):
        if point.x not in self.coordinates:
            self.coordinates[point.x] = dict()

        if point.y in self.coordinates[point.x]:
            self.coordinates[point.x][point.y] += 1
        else:
            self.coordinates[point.x][point.y] = 1

    def addLine(self, line: Line):
        for point in line.interpolate():
            self.addPoint(point)

main()
