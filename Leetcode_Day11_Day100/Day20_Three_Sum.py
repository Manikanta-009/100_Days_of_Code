# 100 Days of Code Challenge

## Day 20: 3Sum (Leetcode)

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)  # Sort the input array
        
        for i in range(len(nums)):
            # Skip duplicates for the first element of the triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1  # Initialize left pointer
            right = len(nums) - 1  # Initialize right pointer
            
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]

                if total_sum > 0:
                    right -= 1  # Decrease right pointer for a smaller sum
                elif total_sum < 0:
                    left += 1  # Increase left pointer for a larger sum
                else:
                    result.append([nums[i], nums[left], nums[right]])  # Found a triplet
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for the second and third elements of the triplet
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    
        return result

solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
result = solution.threeSum(nums)
print(result)

"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""