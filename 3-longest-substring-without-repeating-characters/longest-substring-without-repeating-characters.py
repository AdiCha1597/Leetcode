# Brute Force Approach:
# Check every possible substring and determine if it has all unique characters.
# Keep track of the length of the longest substring with unique characters found.
# Time Complexity: O(n^3) as generating all substrings takes O(n^2) and checking each substring for uniqueness takes O(n).
# Space Complexity: O(n) as we may need additional space to store unique characters in a substring.

# Optimized Approach:
# Use a sliding window with two pointers to find the longest substring without repeating characters.
# - Maintain a set to store characters in the current substring.
# - As you iterate over each character with the right pointer (r), check if it already exists in the set.
#   - If it does, move the left pointer (l) to the right, removing characters from the set until there are no duplicates.
# - Update the result with the maximum length found at each step.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()  # Set to store characters in the current substring
        l = 0  # Left pointer for the sliding window
        res = 0  # Variable to store the length of the longest substring

        for r in range(len(s)):  # Iterate over each character with the right pointer
            # If character at right pointer is in the set, adjust the left pointer
            while s[r] in charSet:
                charSet.remove(s[l])  # Remove character at left pointer from the set
                l += 1  # Move the left pointer to the right
            charSet.add(s[r])  # Add current character to the set
            res = max(res, r - l + 1)  # Update the result with the maximum length found

        return res  # Return the length of the longest substring without repeating characters

# Time Complexity: O(n), where n is the length of the string, as each character is added and removed from the set at most once.
# Space Complexity: O(min(n, m)), where m is the character set size (e.g., 26 for lowercase English letters).
