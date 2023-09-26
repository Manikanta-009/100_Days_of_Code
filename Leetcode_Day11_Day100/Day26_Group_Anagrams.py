# 100 Days of Code Challenge

## Day 26: Group Anagrams (Leetcode)

# Import the List class from the typing module
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        # Create a dictionary to store anagrams grouped by their sorted representation.
        anagram_groups = {}

        for word in strs:
            # Sort the characters in the word and join them to create a sorted representation.
            sorted_word = ''.join(sorted(word))

            # If the sorted representation exists in the dictionary, append the word to the group.
            # Otherwise, create a new group for this sorted representation.
            if sorted_word in anagram_groups:
                anagram_groups[sorted_word].append(word)
            else:
                anagram_groups[sorted_word] = [word]

        # Convert the values (groups of anagrams) of the dictionary to a list.
        result = list(anagram_groups.values())

        return result

# Create an instance of the Solution class
solution_instance = Solution()

# Call the groupAnagrams method with a list of strings as an argument
input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagram_groups = solution_instance.groupAnagrams(input_strings)

# Print the result
print(anagram_groups)


"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""