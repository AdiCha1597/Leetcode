class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Approach:
        - Use a sliding window technique to find the length of the longest substring without repeating characters.
        - Use a set to keep track of characters in the current window.
        - Adjust the window size dynamically by moving the left pointer when a duplicate character is found.
        """

        charSet = set()  # Set to store unique characters in the current window
        res = 0  # Result variable to store the length of the longest substring
        l = 0  # Left pointer for the sliding window

        # Iterate over the string with the right pointer
        for r in range(len(s)):
            # While the character at the right pointer is already in the set
            while s[r] in charSet:
                charSet.remove(s[l])  # Remove the character at the left pointer from the set
                l += 1  # Move the left pointer to the right

            # Add the character at the right pointer to the set
            charSet.add(s[r])

            # Update the result with the maximum length found
            res = max(res, r - l + 1)

        return res  # Return the length of the longest substring without repeating characters

# Time Complexity: O(n), where n is the length of the string. Each character is processed at most twice (once by the right pointer and once by the left pointer).
# Space Complexity: O(min(n, m)), where n is the length of the string and m is the size of the character set. In the worst case, the set can contain all unique characters of the string.




        