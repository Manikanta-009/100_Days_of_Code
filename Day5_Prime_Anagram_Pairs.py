# 100 Days of Code Challenge

## Day 5: Prime Anagram Pairs Challenge

### Challenge Description
"""
Write a Python program to find all prime number anagram pairs within a given range.

A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself.

An anagram is a word or phrase formed by rearranging the letters of another.

Input:
- Two positive integer values, 'start' and 'end', defining the range within which to find prime anagram pairs.

Output:
- For each prime anagram pair found in the range, print the pair.

Example Input:
start = 2
end = 100

Example Output:
Prime Anagram Pair: (13, 31)
Prime Anagram Pair: (17, 71)
Prime Anagram Pair: (37, 73)
Prime Anagram Pair: (79, 97)

"""
### Solution Code

def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number**0.5)+1):
        if number % divisor == 0:
            return False
    return True

def sorted_anagram_representation(number):
    return ''.join(sorted(str(number)))

def find_prime_anagram(start, end):
    prime_numbers = [number for number in range(start, end) if is_prime(number)]
    anagram_dict = dict()
    for prime in prime_numbers:
        anagram = sorted_anagram_representation(prime)
        if anagram in anagram_dict:
            anagram_dict[anagram].append(prime)
        else:
            anagram_dict[anagram] = [prime]

    anagram_pairs_result = [tuple(pair) for pair in anagram_dict.values() if len(pair) >= 2]
    result = ''
    for pair in anagram_pairs_result: 
        result += f"Prime Anagram Pair: {pair}\n"

    return result


if __name__ == '__main__':
    print("Prime Anagram Pairs Challenge Solution")
    print("-" * 40)

    start, end = 2, 100

    print(f"Finding prime anagram pairs between {start} and {end}:\n")
    prime_anagrams = find_prime_anagram(start, end)

    if prime_anagrams:
        print("Prime Anagram Pairs:\n" + prime_anagrams)
    else:
        print("No prime anagram pairs found in the given range.")

"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""