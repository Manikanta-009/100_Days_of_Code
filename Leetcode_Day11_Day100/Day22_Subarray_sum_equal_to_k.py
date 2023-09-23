# 100 Days of Code Challenge

## Day 22: Subarray Sum Equals K (Leetcode)

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize a dictionary to store the cumulative sum occurrences
        occurrence = {0:1}
        # Initialize the cumulative sum and the count of subarrays
        prefix_sum = 0
        subarrays_count = 0
        
        for i in range(len(nums)):
            # Update the cumulative sum
            prefix_sum += nums[i]
            # Calculate the value to be removed to reach the target sum k
            remove = prefix_sum - k
            # Increment the subarrays count with occurrences of the 'remove' value
            subarrays_count += occurrence.get(remove, 0)
            # Update the occurrence of the current cumulative sum
            occurrence[prefix_sum] = occurrence.get(prefix_sum, 0) + 1

        return subarrays_count

# Define an instance of the Solution class
solution_instance = Solution()

# Example input
nums = [1, 2, 3, 4, 5]
k = 5

# Call the subarraySum method on the instance
result = solution_instance.subarraySum(nums, k)

# Print the result
print(result)


"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""