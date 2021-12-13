import io
import sys

from typing import List

LLNode = "Node"

def main():
    input_file = sys.argv[1]
    with io.open(input_file,"r") as f:
        input_data = [x.strip("\n") for x in f]

    node_graph = LinkedList()
    node_graph.process_edges(input_data)

    paths = find_paths(node_graph.head, set(), "end")
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

def find_paths(node: LLNode, traversed: set[str], target: str) -> List[List[str]]:
    paths = []
    if node.value == target:
        path = list(traversed)
        path.append(node.value)
        paths.append(path)
        return paths

    for c in node.connections:
        if c.value.islower() and c.value in traversed:
            continue

        skip_node = set()
        skip_node.add(node.value)
        skip_node.update(traversed)
        descendents = find_paths(c, skip_node, target)
        paths.extend(descendents)

    out = traversed
    out.add(node.value)
    paths.append(list(out))
    return paths

main()
