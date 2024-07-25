from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Approach:
        - Compare characters of each string at the same index to find the common prefix.
        - Iterate through the characters of the first string and compare with the characters 
        at the same index in the other strings.
        - If a mismatch is found, return the common prefix found so far.
        - If the end of any string is reached or all characters match, add the character to the result.
        """

        res = ""  # Result to store the longest common prefix

        # Iterate through the characters of the first string
        for i in range(len(strs[0])):
            # Compare the character at index i in all strings
            for s in strs:
                # If index i is out of range for string s or characters do not match
                if i == len(s) or s[i] != strs[0][i]:
                    return res  # Return the longest common prefix found so far

            # If all characters match, add the character to the result
            res += strs[0][i]

        return res  # Return the longest common prefix
    
"""
Time Complexity: O(n * m), where n is the number of strings and m is the length of the shortest string.

Space Complexity: O(1), constant space used as no additional data structures are required except for the result variables.
"""