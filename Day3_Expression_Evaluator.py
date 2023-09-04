# 100 Days of Code Challenge

## Day 3: Expression Evaluation Challenge

### Challenge Description
"""
Write a Python program to evaluate a given mathematical expression.

Input:
- A string containing numbers and operators separated by spaces.

Output:
- If the expression format is invalid, print "Invalid expression format." and terminate the program.
- Otherwise, print the input string, the calculation steps, and the final result.

The expression is valid if:
- The first and last characters are digits.
- All numbers are non-negative integers.
- All operators are +, -, *, /, or %.

Example Input:
"1 * 2 * 12 / 6 / 0 + 12 % 9"

Example Output:
Input string: 1 * 2 * 12 / 6 / 0 + 12 % 9

Calculation steps:
1 * 2 = 2
2 * 12 = 24
24 / 6 = 4.0
4.0 / 0 = 0
0 + 12 = 12
12 % 9 = 3

Final result: 3
"""
### Solution Code

# Define a function to perform calculations based on operands
def perform_calculation(left_operand, right_operand, operator):
    if operator == '+':
        return left_operand + right_operand
    elif operator == '-':
        return left_operand - right_operand
    elif operator == '*':
        return left_operand * right_operand
    # for divison if it is division by 0 we simply return 0 instead of throwing error 
    elif operator == '/':
        if right_operand != 0:
            return left_operand / right_operand
        else:
            return 0
    elif operator == '%':
        return left_operand % right_operand

# Example expression
expression = '1 * 2 * 12 / 6 / 0 + 12 % 9'
expression_list = expression.split()

# Separate operators and numbers
operators = [expression_list[i] for i in range(1, len(expression_list), 2)]
numbers = [expression_list[i] for i in range(0, len(expression_list), 2)]

# Check if expression format is valid
are_numbers_valid = all(number.isdigit() for number in numbers)
are_boundary_chars_digits = all(char.isdigit() for char in (expression[0], expression[-1]))
are_operators_valid = all(operator in '+-*/%' and len(operator)==1 for operator in operators)
is_length_valid = len(numbers) == len(operators) + 1

# Check if any of the format checks failed
if not (are_numbers_valid and are_boundary_chars_digits and are_operators_valid and is_length_valid):
    print("Expression format is invalid.")
    exit()


# Initialize index, left operand, and result
index = 0
left_operand = int(numbers[0])  # Initialize the left operand with the first number
result = left_operand  # Initialize the result with the value of the left operand

# Print the input string
print(f"Input string: {expression}\n")

# Print calculation steps
print("Calculation steps:")
while index < len(operators):
    right_operand = int(numbers[index + 1])  # Get the next number as the right operand
    operator = operators[index]  # Get the operator
    
    # Perform the calculation
    result = perform_calculation(left_operand, right_operand, operator)
    
    # Print the calculation step
    print(f"{left_operand} {operator} {right_operand} = {result}")
    
    # Update the left operand for the next iteration
    left_operand = result
    
    index += 1

# Print the final result
print("\nFinal result:", result)

"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""