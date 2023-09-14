# 100 Days of Code Challenge

## Day 13: Contains Duplicate (Leetcode)
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create an empty set to store unique numbers
        hash_set = set()
        
        # Iterate through the input list 'nums'
        for number in nums:
            # Check if the current number is already in the 'hash_set'
            if number in hash_set:
                # If it is, return True indicating that a duplicate exists
                return True
            else:
                # If it's not in the set, add it to the 'hash_set'
                hash_set.add(number)
        
        # If the loop completes without finding any duplicates, return False
        return False

solution = Solution()
nums = [1, 2, 3, 4, 5]
result = solution.containsDuplicate(nums)
print(result)  # This will print False because there are no duplicates in the list.

nums = [1, 2, 3, 4, 1]
result = solution.containsDuplicate(nums)
print(result)  # This will print True because there is a duplicate

"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""