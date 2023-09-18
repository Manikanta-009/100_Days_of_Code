# 100 Days of Code Challenge

## Day 18: Find Minimum in Rotated Sorted Array (Leetcode)

from typing import List

class Solution:
    def findMin(self, nums):
        start, end = 0, len(nums) - 1

        while start < end:
            mid = (start + end) // 2  # Calculate the middle index.

            if nums[mid] > nums[end]:
                # If the middle element is greater than the rightmost element,
                # the minimum must be on the right side.
                start = mid + 1
            elif nums[mid] < nums[end]:
                # If the middle element is less than the rightmost element,
                # the minimum can be on the left side or it could be the middle element itself,
                # so we update the end pointer to mid.
                end = mid
            else:
                # If nums[mid] == nums[end], we don't know which side the minimum is on,
                # but we can safely exclude the rightmost element.
                end -= 1

        return nums[start]  # start and end will point to the minimum element.

# Create an instance of the Solution class
solution = Solution()

# Example usage:
nums = [3,4,5,1,2]
result = solution.findMin(nums)
print("Minimum element:", result)

"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""