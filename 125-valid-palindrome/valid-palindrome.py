import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum()).lower()

        i, j = 0 , len(s)-1
        while i <= j:
            if s[i] != s[j]:
                print('Comparing:', s[i], 'and ', s[j])
                return False
            else:
                i += 1
                j -= 1
        return True

"""
Approach: 
1. Remove all the non-alphanum character from the string and covert the upeercase chars to lowercase.
2. Use two pointers (one at either end)
3. stop checking if chars at the both the pointers are not equal.

a. Time Complexity: O(n) because the regular expression substitution and character comparison each process the string once.
b. Space Complexity: O(n) due to storing the cleaned and lowercased version of the string.
"""

        


        