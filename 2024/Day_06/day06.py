import re
import csv

## Part 1

# Guard = v | < | > | ^ based on orientation
# each obstacle (#) has the guard turn right 90*


# find guard
# determine orientation
# check next spot for obstacles
# if obstacle turn
# move
# if guard moves off map stop and report
class Guard:
    orientation = None
    location = [0, 0]
    blocked = False
    on_map = True


def guard_moves(guard, grid):
    """move the guard until they hit an obstacle"""
    path = [guard.location[0], guard.location[1]]
    grid[guard.location[0]][guard.location[1]] = "X"
    if guard.orientation == up:
        guard.location[0] -= 1
        grid[guard.location[0]][guard.location[1]] = guard.orientation
        if guard.location[0] == 0:
            guard.on_map = False
            path.append(guard.location)
            grid[guard.location[0]][guard.location[1]] = "X"

    elif guard.orientation == down:
        guard.location[0] += 1
        grid[guard.location[0]][guard.location[1]] = guard.orientation
        if guard.location[0] == len(grid) - 1:
            guard.on_map = False
            path.append(guard.location)
            grid[guard.location[0]][guard.location[1]] = "X"

    elif guard.orientation == left:
        guard.location[1] -= 1
        grid[guard.location[0]][guard.location[1]] = guard.orientation
        if guard.location[1] == 0:
            guard.on_map = False
            path.append(guard.location)
            grid[guard.location[0]][guard.location[1]] = "X"

    elif guard.orientation == right:
        guard.location[1] += 1
        grid[guard.location[0]][guard.location[1]] = guard.orientation
        if guard.location[1] == len(grid[0]) - 1:
            guard.on_map = False
            path.append(guard.location)
            grid[guard.location[0]][guard.location[1]] = "X"
    return path


def guard_turns(guard):
    """turn the guard when they hit an obstacle"""
    if guard.orientation == "^":
        guard.orientation = ">"
    elif guard.orientation == ">":
        guard.orientation = "v"
    elif guard.orientation == "v":
        guard.orientation = "<"
    elif guard.orientation == "<":
        guard.orientation = "^"


def locate_guard(data, targets):
    """find where the guard is and facing
    data = map
    targets = possible orientations of the guard
    """
    for i, sublist in enumerate(data):
        for target in targets:
            if target in sublist:
                if target == "^" and data[i - 1][sublist.index(target)] == "#":
                    obstacle = True
                elif target == "v" and data[i + 1][sublist.index(target)] == "#":
                    obstacle = True
                elif target == "<" and data[i][sublist.index(target) - 1] == "#":
                    obstacle = True
                elif target == ">" and data[i][sublist.index(target) + 1] == "#":
                    obstacle = True
                else:
                    obstacle = False
                guard.on_map = True
                return (
                    i,
                    sublist.index(target),
                    target,
                    obstacle,
                )  # Outer index, inner index, and the target
    guard.on_map = False
    return guard.on_map  # If no target is found

    # return position, orientation, path_blocked


def count_string_with_comprehension(data, target):
    return sum(sublist.count(target) for sublist in data)


up, down, left, right = "^", "v", "<", ">"
directions = [up, down, left, right]
# obstacle = "#"

with open("2024\\Day_06\\data.txt", "r") as file:
    # Read each line, strip newline characters, and convert to a list of characters
    grid = [list(line.strip()) for line in file.readlines()]

# starting position
guard = Guard()
pathing = []

while guard.on_map:
    guard.location[0], guard.location[1], guard.orientation, guard.blocked = (
        locate_guard(grid, directions)
    )
    if guard.blocked:
        guard_turns(guard)
    pathing.append(guard_moves(guard, grid))
    # with open("2024\\Day_06\\grid.txt", mode="w", newline="") as file:
    #    writer = csv.writer(file)
    #    writer.writerows(grid)

print(count_string_with_comprehension(grid, "X"))
