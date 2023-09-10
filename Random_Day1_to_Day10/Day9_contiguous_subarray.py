# 100 Days of Code Challenge

## Day 9: Contiguous Subarray with Largest Sum

### Challenge Description
"""
Given an array of integers, find the contiguous subarray with the largest sum. Return the sum and the subarray.

Input:
- 'nums' (list of integers): An array of integers.

Output:
- 'max_sum' (int): The sum of the maximum subarray.
- 'max_subarray' (list of integers): The maximum subarray.

Example Input:
nums = [1, 1, -3, 6, 8, -9]

Example Output:
max_sum = 14
max_subarray = [6, 8]
"""
### Solution Code

def find_max_subarray(nums):
    max_sum = 0
    current_sum = 0
    start_index = 0
    end_index = -1

    for index, num in enumerate(nums):
        if current_sum <= 0:
            current_sum = num
            start_index = index
        else:
            current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum
            end_index = index

    max_subarray = nums[start_index:end_index + 1]
    return max_sum, max_subarray

# Example 1
nums1 = [1, 1, -3, 6, 8, -9]
max_sum1, max_sub_array1 = find_max_subarray(nums1)
print("Input Array:", nums1)
print("Maximum Subarray Sum:", max_sum1)
print("Maximum Subarray:", max_sub_array1)  # Output: 14, [ 6, 8]

# Example 2
nums2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum2, max_sub_array2 = find_max_subarray(nums2)
print("\nInput Array:", nums2)
print("Maximum Subarray Sum:", max_sum2)
print("Maximum Subarray:", max_sub_array2)  # Output: 6, [4, -1, 2, 1]

"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""
