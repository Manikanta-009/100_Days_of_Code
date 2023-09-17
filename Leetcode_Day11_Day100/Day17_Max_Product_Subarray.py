# 100 Days of Code Challenge

## Day 17: Max Product Subarray (Leetcode)

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Check if the input list is empty. If so, return 0 as there are no elements to consider.
        if not nums:
            return 0

        # Initialize variables to store the previous maximum product, previous minimum product,
        # and the final result, all with the value of the first element of nums.
        prev_max_product = nums[0]
        prev_min_product = nums[0]
        result = nums[0]

        # Iterate through the elements of the input list nums starting from the second element (index 1).
        for i in range(1, len(nums)):
            # Calculate the current maximum product and current minimum product ending at index i.
            curr_max_product = max(prev_max_product * nums[i], prev_min_product * nums[i], nums[i])
            curr_min_product = min(prev_max_product * nums[i], prev_min_product * nums[i], nums[i])

            # Update the result by taking the maximum of the current maximum product and the current result.
            result = max(result, curr_max_product)

            # Update the previous maximum and minimum products for the next iteration.
            prev_max_product = curr_max_product
            prev_min_product = curr_min_product

        # Return the final result, which represents the largest subarray product.
        return result

# Create an instance of the Solution class
solution = Solution()

# Call the maxProduct method with the example input [2,3,-2,4]
res = solution.maxProduct([2,3,-2,4])

# Print the result
print(res) # output: 6 (2*3)


"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""