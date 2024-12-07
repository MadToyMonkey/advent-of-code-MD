## Part 1
def find_words_multiple(grid, words):
    rows = len(grid)
    cols = len(grid[0])

    # Define 8 possible directions (row_offset, col_offset)
    directions = [
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0),  # Down
        (-1, 0),  # Up
        (1, 1),  # Down-Right
        (-1, -1),  # Up-Left
        (1, -1),  # Down-Left
        (-1, 1),  # Up-Right
    ]

    def is_valid(x, y):
        """Check if coordinates are within bounds."""
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x, y, word):
        """Search for a word starting from (x, y) in all directions."""
        positions = []
        for row_offset, col_offset in directions:
            nx, ny = x, y
            match = True
            for char in word:
                if not is_valid(nx, ny) or grid[nx][ny] != char:
                    match = False
                    break
                nx += row_offset
                ny += col_offset
            if match:
                # If a match is found, record the start position and direction
                positions.append((x, y, row_offset, col_offset))
        return positions

    # Result dictionary
    found_words = {word: [] for word in words}

    # Search for each word
    for word in words:
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == word[0]:
                    occurrences = search_from(i, j, word)
                    if occurrences:
                        found_words[word].extend(occurrences)

    return found_words


def import_grid(file_path):
    with open(file_path, "r") as file:
        # Read each line, strip newline characters, and convert to a list of characters
        grid = [list(line.strip()) for line in file.readlines()]
    return grid


# Path to the .txt file
file_path = "2024\\Day_04\\data.txt"

# Import the grid
word_search_grid = import_grid(file_path)

# Print the grid to verify
# for row in word_search_grid:
#    print(row)

# Words to find
word_list = ["XMAS"]

# Solve word search
results = find_words_multiple(word_search_grid, word_list)

# Print results
for words, position in results.items():
    if position:
        print(
            f"Word '{words}' found {len(position)} times"
        )  # at positions: {position}")
    else:
        print(f"Word '{words}' not found")


## Part 2
def find_diagonal_x_for_word(grid, word):
    rows = len(grid)
    cols = len(grid[0])

    # Define diagonal directions
    directions = [
        (1, 1),  # Down-Right
        (-1, -1),  # Up-Left
        (1, -1),  # Down-Left
        (-1, 1),  # Up-Right
    ]

    def is_valid(x, y):
        """Check if coordinates are within bounds."""
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x, y, word, direction):
        """Search for a word starting from (x, y) in a single diagonal direction."""
        row_offset, col_offset = direction
        nx, ny = x, y
        path = []
        for char in word:
            if not is_valid(nx, ny) or grid[nx][ny] != char:
                return None  # Invalid path
            path.append((nx, ny))
            nx += row_offset
            ny += col_offset
        return path

    def verify_x_shape(paths):
        """Verify if any two paths form an 'X' by intersecting at their midpoints."""
        midpoints = {
            tuple(path[len(path) // 2]) for path in paths
        }  # Extract all midpoints
        # Check if any midpoint is shared between two paths
        result = []
        for i in range(len(paths)):
            for j in range(i + 1, len(paths)):
                mid1 = paths[i][len(paths[i]) // 2]
                mid2 = paths[j][len(paths[j]) // 2]
                if mid1 == mid2:  # Shared midpoint
                    result.append((paths[i], paths[j]))
        return result

    # Search for all diagonal occurrences of the word
    all_paths = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]:  # Starting point must match the first letter
                for direction in directions:
                    path = search_from(i, j, word, direction)
                    if path:
                        all_paths.append(path)

    # Verify which paths form 'X' shapes
    x_shapes = verify_x_shape(all_paths)
    return x_shapes


# Word to find
word = "MAS"

# Solve word search for 'X' shape
results = find_diagonal_x_for_word(word_search_grid, word)

# Print results
if results:
    print(f"\nTotal 'X' shapes found: {len(results)}")
else:
    print(f"Word '{word}' does not form an 'X' in the grid.")
