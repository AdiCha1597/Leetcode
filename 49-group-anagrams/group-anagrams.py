# Brute Force Approach:
# For each word in the list, compare it with every other word to check if they are anagrams by sorting both words.
# Group words that are anagrams together into separate lists.
# Time Complexity: O(n^2 * k log k), where n is the number of words and k is the maximum length of a word (sorting each word).
# Space Complexity: O(n * k), as we may need to store each word in the resulting lists.

# Optimized Approach:
# 1. Initialize a defaultdict(list) for storing each sorted word as the key and corresponding anagram words as the values.
# 2. For each word in the input list, sort the characters to get a key and append the original word to the list at that key in the map.
# 3. Finally, return the values of the dictionary, which are lists of grouped anagrams.

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to store sorted words as keys and lists of anagrams as values
        anagram_map = defaultdict(list)  

        # Iterate through each word
        for word in strs:

            # Sort characters in the word to form the key
            sorted_word = "".join(sorted(word)) 
            
            # Append the word to the corresponding list in the dictionary 
            anagram_map[sorted_word].append(word)  
        
        # Return all lists of grouped anagrams
        return list(anagram_map.values())  

# Time Complexity: O(n * k log k), where n is the number of words and k is the maximum length of a word. Sorting each word takes O(k log k).
# Space Complexity: O(n * k), where n is the number of words and k is the maximum length of a word, as we store all words in the dictionary.