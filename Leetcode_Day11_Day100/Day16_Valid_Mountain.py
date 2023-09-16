# 100 Days of Code Challenge

## Day 15: Valid Mountain Array (Leetcode)

from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)

        if n < 3:
            return False
        
        left = 0
        right = n - 1

        # Move the left pointer to find the increasing part of the mountain
        while left < n - 1 and arr[left] < arr[left + 1]:
            left += 1
        
        # Move the right pointer to find the decreasing part of the mountain
        while right > 0 and arr[right] < arr[right - 1]:
            right -= 1

        # Check if both pointers met at the same index and not at the start or end
        return left == right and left > 0 and right < n - 1

# Example usage:
solution_instance = Solution()
input_array = [0, 3, 2, 1]
is_valid_mountain = solution_instance.validMountainArray(input_array)
print(is_valid_mountain)  # This will print True for the provided input array

"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""