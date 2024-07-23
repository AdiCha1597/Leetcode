from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Approach:
        - Count the frequency of each character in the string.
        - For each character with an even frequency, add that count to the result.
        - For characters with an odd frequency, add the even part of that count to the result.
        - If there is at least one character with an odd frequency, add one to the result to account for the center of the palindrome.
        """

        char_count = defaultdict(int)  # Initialize a defaultdict to count characters
        res = 0  # Result to store the length of the longest palindrome

        # Count frequencies of each character
        for char in s:
            char_count[char] += 1  # Increment the count for the character
            if char_count[char] % 2 == 0:  # If the count is even
                res += 2  # Add 2 to the result (pair of characters can form a palindrome)

        # Check if there is any character with an odd frequency
        for value in char_count.values():
            if value % 2 == 1:  # If there is at least one character with an odd frequency
                res += 1  # Add one to the result to place this character in the center
                break  # Only one odd frequency character can be in the center

        return res  # Return the result

# Time Complexity: O(n), where n is the length of the string (due to single pass through the string and the character counts).
# Space Complexity: O(1), since the dictionary will have at most 52 keys (for all lowercase and uppercase English letters).

