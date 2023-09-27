# 100 Days of Code Challenge

## Day 27: Longest Palindromic Substring (Leetcode)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Store the longest palindromic substring found
        longest_palindrome = ""  
        # Store the length of the longest palindromic substring
        max_palindrome_length = 0  

        for i in range(len(s)):
            # Odd Index Palindromes
            # Initialize left and right pointers to the current index
            left, right = i, i  
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # Check if the current palindrome is longer than the previous longest
                if (right - left + 1) > max_palindrome_length:
                    max_palindrome_length = right - left + 1
                    # Update the longest palindrome substring
                    longest_palindrome = s[left: right + 1]  

                left -= 1  # Expand the palindrome by moving left pointer to the left
                right += 1  # Expand the palindrome by moving right pointer to the right

            # Even Index Palindromes
            # Initialize left and right pointers to adjacent indices
            left, right = i, i + 1  
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # Check if the current palindrome is longer than the previous longest
                if (right - left + 1) > max_palindrome_length:
                    max_palindrome_length = right - left + 1
                    # Update the longest palindrome substring
                    longest_palindrome = s[left: right + 1]  

                left -= 1  # Expand the palindrome by moving left pointer to the left
                right += 1  # Expand the palindrome by moving right pointer to the right

        return longest_palindrome  # Return the longest palindromic substring
        

# Create an instance of the Solution class
solution_instance = Solution()

# Call the longestPalindrome method on the created instance
input_string = "babad"  # Replace with your input string
result = solution_instance.longestPalindrome(input_string)

# Print the result, which is the longest palindromic substring
print(result)



"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""