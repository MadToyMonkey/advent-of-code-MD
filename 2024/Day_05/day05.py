# Part 1
from collections import defaultdict, deque
import numpy as np


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


# Function to filter rules and reorder sets
def reorder_set(input_set, rules):
    # Filter the rules to include only numbers in the input set
    filtered_rules = [(a, b) for a, b in rules if a in input_set and b in input_set]

    # Build graph (adjacency list) and in-degree count
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    nodes = set(input_set)  # Only include relevant nodes

    for a, b in filtered_rules:
        graph[a].append(b)
        in_degree[b] += 1
        if a not in in_degree:
            in_degree[a] = 0

    # Topological sort using Kahn's algorithm
    queue = deque([node for node in nodes if in_degree[node] == 0])
    sorted_order = []

    while queue:
        current = queue.popleft()
        sorted_order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check for cycles
    if len(sorted_order) != len(nodes):
        raise ValueError("Graph has a cycle; cannot sort.")

    return sorted_order


# Read the file into memory
with open("2024\\Day_05\\data.txt", "r") as file:
    sections = file.read().strip().split("\n\n")
# Parse each section using pandas
rules = np.loadtxt(sections[0].splitlines(), delimiter="|").tolist()
pages = [list(map(int, line.split(","))) for line in sections[1].splitlines()]
middles = []
re_middles = []

for e in pages:
    # have to filter the rules to only include the pages in the current set
    filtered_rules = [(a, b) for a, b in rules if a in e and b in e]
    if validate_order(filtered_rules, e):
        middles.append(e[len(e) // 2])
    else:
        re_e = reorder_set(e, filtered_rules)
        re_middles.append(re_e[len(re_e) // 2])
print(f"Originally Correct: {sum(middles)}")
print(f"Originally In-Correct: {sum(re_middles)}")
