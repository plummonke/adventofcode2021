import io
import sys

from collections import Counter
from typing import List

LLNode = "Node"

def main():
    input_file = sys.argv[1]
    with io.open(input_file,"r") as f:
        input_data = [x.strip("\n") for x in f]

    node_graph = LinkedList()
    node_graph.process_edges(input_data)

    paths = find_paths(node_graph.head, [], "end")
    end = list(filter(lambda x: "end" in x, paths))
    print(end)
    print(len(end))

class LinkedList:
    def __init__(self):
        self.head = ""
        self.nodes = {}
    
    def __repr__(self) -> str:
        return f"LinkedList: head = {self.head}"

    def process_edges(self, edges: List[str]):
        split = [x.split("-") for x in edges]
        self.nodes = {x[i]: Node(x[i]) for x in split for i in range(len(x))}
        self.head = self.nodes["start"]

        for a, b in split:
            self.nodes[a].add_connection(self.nodes[b])
            self.nodes[b].add_connection(self.nodes[a])

class Node:
    def __init__(self, value: str):
        self.value = value
        self.connections = set()

    def __repr__(self) -> str:
        return f"Node: {self.value}"

    def add_connection(self, node: LLNode):
        self.connections.add(node)

def find_paths(node: LLNode, traversed: List[str], target: str) -> List[List[str]]:
    paths = []
    if node.value == target:
        path = list(traversed)
        path.append(node.value)
        paths.append(path)
        return paths

    count = Counter(traversed)
    lower_two = list(filter(lambda x: x[0].islower() and int(x[1]) > 1, count.items()))

    for c in node.connections:
        if (len(lower_two) > 0 and node.value.islower() and count[node.value] != 0) or (c.value in ("start","end") and count[c.value] > 0):
            continue

        skip_node = [node.value, ]
        skip_node.extend(traversed)
        descendents = find_paths(c, skip_node, target)
        paths.extend(descendents)

    out = traversed
    out.extend(node.value)
    paths.append(list(out))
    return paths

main()
