# 100 Days of Code Challenge

## Day 20: Container With Most Water (Leetcode)

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1
        max_area = 0
        
        while left_pointer < right_pointer:
            # Calculate the height of the shorter side of the container
            container_height = min(height[left_pointer], height[right_pointer])
            
            # Calculate the width of the container
            container_width = right_pointer - left_pointer
            
            # Calculate the area of the container
            container_area = container_height * container_width
            
            # Update the maximum area if the current area is larger
            max_area = max(max_area, container_area)
            
            # Move the pointers towards each other
            if height[left_pointer] <= height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        
        return max_area

# Create an instance of the Solution class
solution = Solution()

# Example input
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# Calculate and print the result
result = solution.maxArea(heights)
print("The maximum area of a container formed by the given heights is:", result)

"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""