# 100 Days of Code Challenge

## Day 23: Set Matrix Zeroes (Leetcode)

class Solution:
    def setZeroes(self, matrix):
        """
        Modify the matrix in-place by setting rows and columns to 0 based on zero elements.
        """
        num_rows, num_cols = len(matrix), len(matrix[0])

        # Check if the first row and first column contain any zeros
        has_zero_in_first_row = any(matrix[0][col] == 0 for col in range(num_cols))
        has_zero_in_first_col = any(matrix[row][0] == 0 for row in range(num_rows))

        # If a cell contains 0, mark the first row and column accordingly
        for row in range(1, num_rows):
            for col in range(1, num_cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # Update 0 in the corresponding rows based on the presence of 0 in the first column.
        for row in range(1, num_rows):
            if matrix[row][0] == 0:
                for col in range(1, num_cols):
                    matrix[row][col] = 0

        # Update 0 in the corresponding columns based on the presence of 0 in the first row.
        for col in range(1, num_cols):
            if matrix[0][col] == 0:
                for row in range(1, num_rows):
                    matrix[row][col] = 0

        # If the first row has a zero, set the entire row to zero
        if has_zero_in_first_row:
            for col in range(num_cols):
                matrix[0][col] = 0

        # If the first column has a zero, set the entire column to zero
        if has_zero_in_first_col:
            for row in range(num_rows):
                matrix[row][0] = 0

# Example usage:
solution = Solution()
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

print("Original Matrix:")
for row in matrix:
    print(row)

solution.setZeroes(matrix)

print("\nMatrix After Setting Zeroes:")
for row in matrix:
    print(row)

"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""