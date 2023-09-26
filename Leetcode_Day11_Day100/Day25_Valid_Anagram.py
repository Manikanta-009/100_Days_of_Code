# 100 Days of Code Challenge

## Day 25: Valid Anagram (Leetcode)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the lengths of the two strings are different; if so, they can't be anagrams.
        if len(s) != len(t):
            return False
        
        # Create dictionaries to store character counts for both strings.
        s_count = dict()
        t_count = dict()

        # Count the occurrences of each character in string s.
        for char in s:
            s_count[char] = s_count.get(char, 0) + 1 

        # Count the occurrences of each character in string t.
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1 

        # Compare the character counts of both strings.
        return s_count == t_count

# Create an instance of the Solution class
solution = Solution()

# Check if two strings are anagrams
result = solution.isAnagram("listen", "silent")

# Print the result
print(result)  # This will print True because "listen" and "silent" are anagrams


"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""