# 100 Days of Code Challenge

## Day 19: Search in Rotated Sorted Array (Leetcode)

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2  # Calculate the middle index.

            if nums[mid] == target:
                return mid  # Found the target, return its index.

            if nums[start] <= nums[mid]:
                # If the left half is sorted.
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1  # Target is in the left half.
                else:
                    start = mid + 1  # Target is in the right half.
            else:
                # If the right half is sorted.
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1  # Target is in the right half.
                else:
                    end = mid - 1  # Target is in the left half.

        return -1  # Target was not found in the array.

# Example usage:
nums = [4, 5, 6, 7, 0, 1, 2]
target = 6

solution = Solution()
result = solution.search(nums, target)

if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} was not found in the array.")

"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""