matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:             # Outer loop goes through each row
    for element in row:        # Inner loop goes through each element in that row
        print(element, end=' ')
    print()  # For a new line after each row
