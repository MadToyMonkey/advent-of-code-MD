# Part 1
import re

# import corrupted data
pattern = r"mul\((\d+),(\d+)\)"

with open("2024\\Day_03\\data.txt", "r") as f:
    line = f.read()


def product_sum(pattern, text):
    # process massive string
    matches = re.findall(pattern, text)
    # Convert matched digits to integers
    matches = [(int(n1), int(n2)) for n1, n2 in matches]
    # Multiply each pair and sum the products
    total = sum(n1 * n2 for n1, n2 in matches)
    return total


total_sum = product_sum(pattern, line)
print("Part ONE\nSum of products:", total_sum)

# Part 2
patternDO = r"do\(\)"
patternDONT = r"don't\(\)"


def conditional_matchlist(text, pattern1, pattern2, pattern3):
    """
    pattern1 == Do enable
    pattern2 == mul statements
    pattern3 == don't enable
    """
    # Compile patterns
    p1 = re.compile(pattern1)
    p2 = re.compile(pattern2)
    p3 = re.compile(pattern3)

    # Initialize flags and results
    search_for_p2 = True
    results = []

    # Iterate through all matches in the string
    for match in re.finditer(rf"{pattern1}|{pattern2}|{pattern3}", text):
        match_text = match.group()

        if p1.fullmatch(match_text):  # Found pattern1
            search_for_p2 = True
        elif p3.fullmatch(match_text):  # Found pattern3
            search_for_p2 = False
        elif (
            p2.fullmatch(match_text) and search_for_p2
        ):  # Found pattern2 while searching for it
            results.append(match_text)
    return results


data = conditional_matchlist(line, patternDO, pattern, patternDONT)

print("Part TWO\nSum of products:", product_sum(pattern, str(data)))
