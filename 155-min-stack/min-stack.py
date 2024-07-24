class MinStack:

    def __init__(self):
        """
        Initialize the data structure.
        - stack: a list to store the stack elements.
        - m: a list to store the minimum values corresponding to each element in the stack.
        """
        self.stack = []  # Main stack to store elements
        self.m = []  # Stack to store minimum values

    def push(self, val: int) -> None:
        """
        Push the element val onto the stack.
        - Append val to the main stack.
        - Compute the new minimum (the minimum of val and the current minimum).
        - Append the new minimum to the min stack.
        """
        self.stack.append(val)  # Add value to the main stack
        val = min(val, self.m[-1] if self.m else val)  # Compute the new minimum
        self.m.append(val)  # Add the new minimum to the min stack

    def pop(self) -> None:
        """
        Remove the element on top of the stack.
        - Pop the top element from both the main stack and the min stack.
        """
        self.stack.pop()  # Remove the top element from the main stack
        self.m.pop()  # Remove the top element from the min stack

    def top(self) -> int:
        """
        Get the top element of the stack.
        - Return the top element from the main stack.
        """
        return self.stack[-1]  # Return the top element

    def getMin(self) -> int:
        """
        Retrieve the minimum element in the stack.
        - Return the top element from the min stack.
        """
        return self.m[-1]  # Return the current minimum

# Time Complexity:
# - push method: O(1), as appending to both stacks is an O(1) operation.
# - pop method: O(1), as popping from both stacks is an O(1) operation.
# - top method: O(1), as accessing the last element is an O(1) operation.
# - getMin method: O(1), as accessing the last element of the min stack is an O(1) operation.

# Space Complexity: O(n), where n is the number of elements pushed onto the stack.
# Both stacks grow linearly with the number of elements.
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()