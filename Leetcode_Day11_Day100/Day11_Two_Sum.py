# 100 Days of Code Challenge

## Day 11: Two Sum (Leetcode)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store values and their corresponding indices
        two_sum = dict()

        # Iterate through the list of numbers along with their indices
        for indx, num in enumerate(nums):
            # Calculate the difference between the target and the current number
            check = target - num
            
            # Check if the 'check' value is already in the dictionary
            if check in two_sum:
                # If it is, return the indices of the two numbers that sum up to the target
                return [two_sum[check], indx]
            else:
                # If not, store the current number and its index in the dictionary
                two_sum[num] = indx

# Example usage:
# Create an instance of the Solution class
sum = Solution()
# Call the twoSum method to find the indices of two numbers that add up to the target
result = sum.twoSum([2, 7, 11, 15], 9)
print(result)  # Output should be [0, 1] since nums[0] + nums[1] = 2 + 7 = 9


"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""