import io
import sys

def main():
    input_file = sys.argv[1]
    with io.open(input_file,"r") as f:
        input_data = [x.strip("\n") for x in f]

    coords = (x.split(",") for x in input_data if "," in x)
    folds = (x for x in input_data if "fold" in x)

    points = {tuple(map(int, x)) for x in coords}

    new_graph = points
    for fold in folds:
        axis = parse_fold(fold)
        new_graph = fold_graph(axis[0], axis[1], new_graph)

    extents = max_extents(new_graph)
    matrix = [["-" for x in range(extents[0])] for y in range(extents[1])]

    for each in new_graph:
        matrix[each[1]][each[0]] = "x"

    for row in matrix:
        print("".join(row))

def max_extents(points: set[tuple[int,int]]) -> tuple[int,int]:
    x = max([n[0] for n in points])
    y = max([n[1] for n in points])
    return (x + 1, y + 1)

def fold_graph(axis: str, index: int, points: set) -> set[(int, int)]:
    i = {"x":0,"y":1}[axis]
    under = set(filter(lambda x: x[i] <= index, points))
    over = filter(lambda x: x[i] > index, points)

    out = set()
    for j, point in enumerate(over):
        p = list(point)
        p[i] -= (p[i] - index) * 2
        out.add(tuple(p))

    under.update(out)
    return under

def parse_fold(fold: str) -> tuple[str, int]:
    terms = fold.split()
    axis = terms[-1].split("=")
    axis[1] = int(axis[1])
    return tuple(axis)

main()
