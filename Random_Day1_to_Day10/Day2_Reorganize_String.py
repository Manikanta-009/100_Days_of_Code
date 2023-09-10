# 100 Days of Code Challenge

## Day 2: Reorganize String Challenge

### Challenge Description
"""
Problem Description: Reorganize String

You are given a string 's' consisting of lowercase English letters. 
Your task is to reorganize the characters in the string in such a way that no two adjacent characters are the same. 
If it is not possible to reorganize the string to meet this condition, return an empty string.

Input:
- A string 's' containing lowercase English letters.

Output:
- Return a string where the characters are reorganized according to the rule above.
- If it is not possible to reorganize the string, return an empty string.

Example Input:
"aabcddaaa"

Example Output:
Reorganized: "adadabaca"

Note:
In the example input, the most frequent character is 'a' with a count of 5, and the total count of characters is 9.
Since 5 is not more than half of 9, reorganization is possible.
One possible reorganized string is "acadadaab" where no two adjacent characters are the same.
"""
### Solution Code

from collections import Counter

def reorganize_string(s):
    # Count the occurrences of each character in the string
    char_counts = Counter(s)
    
    # Sort characters based on their frequency in descending order
    sorted_chars = sorted(char_counts, key=lambda char: char_counts[char], reverse=True)
    
    # Get the most frequent character count
    max_count = char_counts[sorted_chars[0]]
    
    # Get the total count of characters in the input string
    total_count = len(s)

    # Check if the most frequent character count exceeds the limit for reorganization
    if max_count > (total_count + 1) // 2:
        return ""

    # Initialize an array to hold the reorganized string
    result = [''] * total_count
    even_index, odd_index = 0, 1

    # Reorganize the characters by alternating even and odd indices
    for char in sorted_chars:
        count = char_counts[char]

        while count > 0 and even_index < total_count:
            result[even_index] = char
            count -= 1
            even_index += 2

        while count > 0 and odd_index < total_count:
            result[odd_index] = char
            count -= 1
            odd_index += 2

    # Convert the array to a string and return
    return ''.join(result)

# Example input string
input_string = "aabcddaaa"

# Call the reorganize_string function
output = reorganize_string(input_string)
print("input string:", input_string)
# Check if reorganization was successful and print the result
if output:
    print("Reorganized:", output)
else:
    print("Cannot reorganize.")

"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""
