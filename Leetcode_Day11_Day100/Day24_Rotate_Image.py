# 100 Days of Code Challenge

## Day 24: Rotate Image (Leetcode)

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Get the size of the matrix (assuming it's a square matrix)
        n = len(matrix)
        
        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                # Swap the elements at (i, j) and (j, i)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row to complete the rotation
        for i in range(n):
            # Reverse the ith row using list slicing (matrix[i][::-1])
            matrix[i] = matrix[i][::-1]

# Input matrix (example)
input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Create a Solution object
solution = Solution()

# Rotate the input matrix in-place
solution.rotate(input_matrix)

# Print the rotated matrix
for row in input_matrix:
    print(row)


"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""