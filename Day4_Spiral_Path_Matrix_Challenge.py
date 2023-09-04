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

def spiralPathMatrix(matrix, row_count, coloumn_count):
    row_begin, row_end = 0, row_count - 1
    column_begin, column_end = 0, coloumn_count - 1
    result = []

    while row_begin <= row_end and column_begin <= column_end:
        for index in range(column_begin, column_end + 1):
            result.append(matrix[row_begin][index])
        row_begin += 1

        for index in range(row_begin, row_end + 1):
            result.append(matrix[index][column_end])
        column_end -= 1

        if row_begin <= row_end:
            for index in range(column_end, column_begin - 1, -1):
                result.append(matrix[row_end][index])
        row_end -= 1

        if column_begin <= column_end:
            for index in range(row_end, row_begin - 1, -1):
                result.append(matrix[index][column_begin])
        column_begin += 1

    return result


matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
    [26, 27, 28, 29, 30]
]

row, column = len(matrix), len(matrix[0])
result = spiralPathMatrix(matrix, row, column)

print("Input Matrix:")
for row in matrix:
    print(row)
    
print("\nSpiral Path Result:")
print(result)

"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""