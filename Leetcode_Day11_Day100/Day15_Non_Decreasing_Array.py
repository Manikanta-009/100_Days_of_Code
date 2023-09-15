# 100 Days of Code Challenge

## Day 15: Non-decreasing Array (Leetcode)

from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0  # Initialize a count to keep track of the number of modifications

        # Iterate through the array, comparing adjacent elements
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:  # If the current element is greater than the next one
                count += 1  # Increment the count of modifications
                if count > 1:  # If more than one modification is needed, return False
                    return False

                # Try to make a modification to ensure non-decreasing order
                if i > 0 and nums[i - 1] > nums[i + 1]:  # Check the element before and after
                    nums[i + 1] = nums[i]  # Modify the next element to match the current one
                else:
                    nums[i] = nums[i + 1]  # Modify the current element to match the next one

        return True  # If the loop completes, return True (at most one modification needed)

# Example usage:
solution = Solution()
nums = [4, 2, 3]
result = solution.checkPossibility(nums)
print(result)  # Output should be True

nums = [4,2,1]
result = solution.checkPossibility(nums)
print(result)  # Output should be False

"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""