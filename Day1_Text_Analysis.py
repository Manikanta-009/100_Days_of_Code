# 100 Days of Code Challenge

## Day 1: Text Analysis Challenge

### Challenge Description
"""
Write a Python program to analyze a given sentence and extract various statistics.

Input:
- A string containing a sentence.

Output:
- Display the following statistics:
  - The input sentence.
  - The list of words in the sentence.
  - The character count considering only alphabetic characters.
  - The average word length.
  - The count of vowels.
  - The most common words and their frequencies (top 5).
  - The longest word among the most common words.


Example Input:
"Hello! How are you doing today? Hello again!"

Example Output:
Sentence (input):  Hello! How are you doing today? Hello again!
Words: ['Hello', 'How', 'are', 'you', 'doing', 'today', 'Hello', 'again']
Character Count (Alphabetic Only): 34
Average Word Length: 4.25
Vowel Count: 16
Most Common Words: {'hello': 2, 'how': 1, 'are': 1, 'you': 1, 'doing': 1}
Longest Word: hello
"""
### Solution Code

import re

def analyze_text_statistics(sentence):
    # Split the sentence into words using regex to find alphabetic sequences
    words = re.findall(r'[a-zA-Z]+', sentence)

    # Calculate the character count considering only alphabetic characters
    characters_count = sum(len(word) for word in words)

    # Calculate the average word length
    word_len = [len(word) for word in words]
    avg_word_len = sum(word_len) / len(words)

    # Count the number of vowels in the sentence
    vowel_count = len([ch for word in words for ch in word if ch.lower() in 'aeiou'])

    # Create a dictionary to store word frequencies
    most_common = {}
    for word in words:
        word = word.lower()
        most_common[word] = most_common.get(word, 0) + 1

    # Sort the most common words by frequency and select the top 5
    most_common_sorted = dict(sorted(most_common.items(), key=lambda item: item[1], reverse=True))
    most_common_first_5 = {key: value for index, (key, value) in enumerate(most_common_sorted.items()) if index < 5}

    # Find the longest word among the most common words
    longest_word = max(most_common_sorted, key=len)

    # Display the results
    print("Sentence (input): ", sentence)
    print("Words:", words)
    print("Character Count (Alphabetic Only):", characters_count)
    print("Average Word Length:", avg_word_len)
    print("Vowel Count:", vowel_count)
    print("Most Common Words:", most_common_first_5)
    print("Longest Word:", longest_word)

if __name__ == "__main__":
    sentence = "Hello! How are you doing today? Hello again!"
    analyze_text_statistics(sentence)


"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""