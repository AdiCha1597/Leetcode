class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to simplify handling the result list
        dummy = ListNode()
        current = dummy
        carry = 0

        # Traverse both lists
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            sum_digit = total % 10

            # Append new node to the result list
            current.next = ListNode(sum_digit)
            current = current.next

            # Move to the next nodes in the lists
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

# Simplified Approach in 4 Lines:
        # 1. Traverse both linked lists using pointers, summing nodes' values with carry-over.
        # 2. Add values and previous carry, compute new carry and the digit.
        # 3. Append each sum's result to a new linked list via a dummy node.
        # 4. Move pointers to the next nodes until all nodes are processed, and no carry remains.

        # Time Complexity: O(max(m, n)), where m and n are lengths of the two lists.
        # Space Complexity: O(max(m, n)) to store the result, potentially one extra for a final carry.
