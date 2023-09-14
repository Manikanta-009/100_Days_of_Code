# 100 Days of Code Challenge

## Day 14: Product of Array Except Self (Leetcode)

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Check if the input list is empty
        if not nums:
            return []
        
        length_of_nums = len(nums)
        # Initialize the result list with 1s
        result = [1] * length_of_nums

        product = 1
        # Calculate the product of all elements to the left of each element
        for index in range(length_of_nums):
            result[index] = product  # Store the product of elements to the left
            product *= nums[index]  # Update the product for the next element
        
        product = 1
        # Calculate the product of all elements to the right of each element
        for index in range(length_of_nums - 1, -1, -1):
            result[index] *= product  # Multiply by the product of elements to the right
            product *= nums[index]  # Update the product for the next element

        return result

# Example usage:
nums = [1, 2, 3, 4]
solution = Solution()
result = solution.productExceptSelf(nums)
print(result)  # Output will be [24, 12, 8, 6]


"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""