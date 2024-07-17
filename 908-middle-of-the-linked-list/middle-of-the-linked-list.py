# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Finds the middle node of a singly linked list in one pass.
        """

        if not head:  # Handle empty list case
            return None

        slow, fast = head, head

        # Traverse the list using two pointers:
        # - slow: Moves one step at a time.
        # - fast: Moves two steps at a time (if possible).
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

        """
        **Time Complexity:** O(n), where n is the number of nodes in the linked list.
        The algorithm iterates through the list once, visiting each node at most
        once. This is the optimal time complexity for finding the middle node
        without additional data structures.

        **Space Complexity:** O(1), constant space.
        The algorithm only uses two pointers, `slow` and `fast`, which are
        independent of the input size. This is a space-efficient approach.
        """




        