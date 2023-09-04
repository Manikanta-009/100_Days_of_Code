# 100 Days of Code Challenge

## Day 4: Spiral Path Matrix Challenge

### Challenge Description
"""
Given a matrix of integers, your task is to traverse the matrix in a spiral path starting from the top-left corner and moving towards the center in a clockwise direction.

Input:
- 'matrix' (list of lists): A matrix of integers.
- 'row_count' (int): Number of rows in the matrix.
- 'coloumn_count' (int): Number of columns in the matrix.

Output:
- 'result' (list): A list containing the elements of the matrix in a spiral path.

Example Input:
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
    [26, 27, 28, 29, 30]
]
row_count = 6
coloumn_count = 5

Example Output:
[1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 29, 28, 27, 26, 21, 16, 11, 6, 7, 8, 9, 14, 19, 24, 23, 22, 17, 12, 13, 18]

Note:
- Ensure that the matrix dimensions are correct.
- The output should contain the elements of the matrix traversed in a spiral path.
"""
### Solution Code

def spiralPathMatrix(matrix, row_count, column_count):
    # Initialize variables to keep track of the current row and column boundaries
    row_begin, row_end = 0, row_count - 1
    column_begin, column_end = 0, column_count - 1
    result = []  # Initialize an empty list to store the spiral path elements

    # Loop until we have covered all rows and columns
    while row_begin <= row_end and column_begin <= column_end:
        # Traverse from left to right along the current row
        for index in range(column_begin, column_end + 1):
            result.append(matrix[row_begin][index])
        row_begin += 1  # Move the row boundary down

        # Traverse from top to bottom along the current column
        for index in range(row_begin, row_end + 1):
            result.append(matrix[index][column_end])
        column_end -= 1  # Move the column boundary left

        # Check if there are more rows to traverse
        if row_begin <= row_end:
            # Traverse from right to left along the current row
            for index in range(column_end, column_begin - 1, -1):
                result.append(matrix[row_end][index])
            row_end -= 1  # Move the row boundary up

        # Check if there are more columns to traverse
        if column_begin <= column_end:
            # Traverse from bottom to top along the current column
            for index in range(row_end, row_begin - 1, -1):
                result.append(matrix[index][column_begin])
            column_begin += 1  # Move the column boundary right

    return result

# Define the input matrix
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
    [26, 27, 28, 29, 30]
]

# Get the number of rows and columns in the matrix
row, column = len(matrix), len(matrix[0])

# Call the spiralPathMatrix function to obtain the result
result = spiralPathMatrix(matrix, row, column)

# Print the input matrix
print("Input Matrix:")
for row in matrix:
    print(row)

# Print the elements in spiral order
print("\nSpiral Path Result:")
print(result)


"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""