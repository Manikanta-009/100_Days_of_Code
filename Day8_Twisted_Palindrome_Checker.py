# 100 Days of Code Challenge

## Day 8: Twisted Palindrome Checker

### Challenge Description
"""
Today's challenge involves building a Python program that determines whether a given word is a "twisted palindrome."

A twisted palindrome is a word that remains the same when its letters are replaced by their corresponding positions
in the English alphabet. For instance, the word "racecar" transforms into the sequence [18, 1, 3, 5, 3, 1, 18] 
based on letter positions.

Your program should:
- Accept a word as input
- Remove spaces and convert the word to lowercase
- Check if the word is a valid input (consisting only of characters, with or without spaces)
- Calculate the sequence of letter positions
- Compare the left and right sides of the sequence to determine if it's a twisted palindrome
"""

### Solution Code

def twisted_palindrome(word):
    # Convert the word to lowercase and remove spaces
    word = word.lower().replace(" ", "")
    
    # Check for valid input
    if not word.isalpha():
        return f"'{word}' is invalid input, please provide characters only"
    
    # Create a sequence representing positions in the English alphabet (a=1, b=2, ..., z=26)
    sequence = [ord(character) - ord('a') + 1 for character in word]
    
    left_character = 0
    right_character = len(word) - 1
    
    while left_character < right_character:
        if sequence[left_character] != sequence[right_character]:
            return f"'{word}' is not a twisted palindrome"
        
        left_character += 1
        right_character -= 1
    
    return f"'{word}' is a twisted palindrome"

if __name__ == "__main__":
    print(twisted_palindrome('Racecar'))  # [18, 1, 3, 5, 3, 1, 18]
    print(twisted_palindrome('Jersey7'))  # Invalid input, please provide characters only
    print(twisted_palindrome('Anna'))     # [1, 14, 14, 1]


"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""
