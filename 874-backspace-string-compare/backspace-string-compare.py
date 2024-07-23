class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Approach:
        Traverse both strings from the end to the beginning.
        Skip characters that are backspaced and compare the remaining characters.
        Use a helper function to find the next valid character index, considering backspaces.
        """

        def getNextValidCharIndex(string: str, index: int) -> int:
            """
            Helper function to find the next valid character index in a string,
            considering backspaces ('#').
            """
            backspace_count = 0  # Initialize backspace counter
            while index >= 0:
                if string[index] == '#':
                    backspace_count += 1  # Increment backspace counter
                elif backspace_count > 0:
                    backspace_count -= 1  # Use one backspace to skip a character
                else:
                    break  # Valid character found
                index -= 1  # Move to the previous character
            return index  # Return the index of the next valid character

        index_s = len(s) - 1  # Start from the end of string s
        index_t = len(t) - 1  # Start from the end of string t

        while index_s >= 0 or index_t >= 0:
            # Find the next valid character index in both strings
            index_s = getNextValidCharIndex(s, index_s)
            index_t = getNextValidCharIndex(t, index_t)

            # Compare the characters at the current valid indices
            if index_s >= 0 and index_t >= 0 and s[index_s] != t[index_t]:
                return False  # Characters do not match

            # Check if one string is exhausted while the other is not
            if (index_s >= 0) != (index_t >= 0):
                return False  # One string is exhausted while the other is not

            # Move to the previous character in both strings
            index_s -= 1
            index_t -= 1

        return True  # All characters matched

# Time Complexity: O(n + m), where n is the length of s and m is the length of t.
# Space Complexity: O(1), constant space used.