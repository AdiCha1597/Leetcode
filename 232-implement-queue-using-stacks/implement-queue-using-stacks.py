class MyQueue:
    def __init__(self):
        self.stack_in = []  # Stack to handle incoming elements
        self.stack_out = []  # Stack to handle outgoing elements

    def push(self, x: int) -> None:
        self.stack_in.append(x)  # Push element to stack_in

    def pop(self) -> int:
        if not self.stack_out:  # Transfer elements if stack_out is empty
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()  # Pop the element from stack_out

    def peek(self) -> int:
        if not self.stack_out:  # Transfer elements if stack_out is empty
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]  # Peek the top element from stack_out

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out  # Check if both stacks are empty

"""
# Time Complexity:
# - push: O(1)
# - pop: Amortized O(1), since each element is moved exactly once from stack_in to stack_out and then popped.
# - peek: Amortized O(1), similar to pop.
# - empty: O(1)

# Space Complexity:
# - O(n), where n is the number of elements in the queue, as both stacks together will store all the elements.
"""


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

