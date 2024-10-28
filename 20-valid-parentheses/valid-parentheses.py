# Approach:
# Use a stack to track opening brackets. For each character in the string:
# - If it is an opening bracket, push it onto the stack.
# - If it is a closing bracket, check if it matches the top of the stack:
#   - If it matches, pop the top of the stack.
#   - If it doesn’t match or if the stack is empty, return False immediately.
# After processing all characters, if the stack is empty, the string is valid; otherwise, it is invalid.

from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []  # Initialize an empty stack to hold opening brackets

        for char in s:  # Iterate through each character in the string
            if char == '(' or char == '[' or char == '{':  # If character is an opening bracket
                stack.append(char)  # Push it onto the stack
            else:  # If character is a closing bracket
                # Check if it matches the top of the stack
                if char == ')' and stack and stack[-1] == '(':  
                    stack.pop()  # Pop the stack if it matches
                elif char == ']' and stack and stack[-1] == '[':  
                    stack.pop()  # Pop the stack if it matches
                elif char == '}' and stack and stack[-1] == '{':  
                    stack.pop()  # Pop the stack if it matches
                else:
                    return False  # Return False if there is no match or the stack is empty

        return not stack  # Return True if stack is empty (all brackets matched), otherwise False

# Time Complexity: O(n), where n is the length of the string, as we only traverse the string once.
# Space Complexity: O(n) in the worst case, if all characters are opening brackets and need to be stored in the stack.