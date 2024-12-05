# Part 1
from collections import defaultdict, deque
import numpy as np
import pandas as pd
from io import StringIO


def validate_order(rules, order):

    # Build a graph and calculate in-degrees
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Build the graph from rules
    for a, b in rules:
        graph[a].append(b)
        in_degree[b] += 1
        in_degree.setdefault(a, 0)  # Ensure all nodes are in the in-degree map

    # Perform topological sort using Kahn's algorithm
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    topological_order = []

    while queue:
        current = queue.popleft()
        topological_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If the graph has a cycle, the topological order won't include all nodes
    if len(topological_order) != len(in_degree):
        raise ValueError("The rules contain a cycle, so no valid order exists.")

    # Check if the input order respects the topological order
    position = {node: i for i, node in enumerate(topological_order)}
    for i in range(len(order) - 1):
        if position[order[i]] > position[order[i + 1]]:
            return False  # Order is invalid

    return True


# Read the file into memory
with open("2024\\Day_05\\test_data.txt", "r") as file:
    sections = file.read().strip().split("\n\n")

# Parse each section using pandas
rule_set = np.loadtxt(sections[0].splitlines(), delimiter="|").tolist()
pages = pd.read_csv(StringIO(sections[1]), header=None).values.tolist()
