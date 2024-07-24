class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Approach:
        - Use the expand around center approach to find the longest palindromic substring.
        - Check both odd-length and even-length palindromes by expanding around each character and between characters.
        - Keep track of the maximum length palindrome found.
        """

        res = ""  # To store the longest palindromic substring
        reslen = 0  # To store the length of the longest palindromic substring

        for i in range(len(s)):
            # Check for odd-length palindromes
            l, r = i, i  # Initialize left and right pointers at the current index
            while l >= 0 and r < len(s) and s[l] == s[r]:  # Expand while the characters are equal
                if (r - l + 1) > reslen:  # Check if the current palindrome is the longest
                    res = s[l:r + 1]  # Update the longest palindromic substring
                    reslen = r - l + 1  # Update the length of the longest palindrome
                l -= 1  # Move left pointer to the left
                r += 1  # Move right pointer to the right

            # Check for even-length palindromes
            l, r = i, i + 1  # Initialize left and right pointers between the current and next index
            while l >= 0 and r < len(s) and s[l] == s[r]:  # Expand while the characters are equal
                if (r - l + 1) > reslen:  # Check if the current palindrome is the longest
                    res = s[l:r + 1]  # Update the longest palindromic substring
                    reslen = r - l + 1  # Update the length of the longest palindrome
                l -= 1  # Move left pointer to the left
                r += 1  # Move right pointer to the right

        return res  # Return the longest palindromic substring

# Time Complexity: O(n^2), where n is the length of the string. This is because we are expanding around each character and each pair of characters.
# Space Complexity: O(1), constant space is used as no additional data structures are required except for the result variables.
        