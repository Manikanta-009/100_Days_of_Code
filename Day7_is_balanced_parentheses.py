# 100 Days of Code Challenge

## Day 7: is_balanced_parentheses Challenge

### Challenge Description
"""
Given a string containing only the characters '(', ')', '{', '}', '[', and ']',
determine if the input string's parentheses are balanced.

Input:
- The input is a string containing parentheses.

Output:
- Return Balaced/Not Balanced based on the parentheses in the input string 

Example Input:
"()[]{}", ([)]

Example Output:
()[]{} is balanced
([)] is not balanced.
"""
### Solution Code

def is_balanced_parentheses(input_string):
    stack = []  # Initialize an empty stack to keep track of opening brackets
    bracket_mapping = {')': '(', '}': '{', ']': '['}  # Mapping of closing to opening brackets
    
    for char in input_string:
        if char in bracket_mapping.values():
            stack.append(char)  # Push opening brackets onto the stack
        elif char in bracket_mapping.keys():
            if not stack or stack[-1] != bracket_mapping[char]:
                return False  # If stack is empty or top of stack doesn't match, parentheses are not balanced
            stack.pop()  # Pop the corresponding opening bracket from the stack
    
    return len(stack) == 0  # If stack is empty at the end, parentheses are balanced

# Test the function
test_strings = ["()", "()[]{}", "(]", "([)]", "{[()]}"]

for s in test_strings:
    if is_balanced_parentheses(s):
        print(f"Input: '{s}' => Output: Balanced")
    else:
        print(f"Input: '{s}' => Output: Not Balanced")
