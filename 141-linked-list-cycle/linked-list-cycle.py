# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


#Approach:
#Use two pointers, slow and fast, starting at the head of the list.
#Move slow one step and fast two steps in each iteration.
#If they meet, there is a cycle; if fast reaches the end, there is no cycle.
#Time Complexity:
#O(n): where n is the number of nodes in the linked list.
#Space Complexity:
#O(1): only a constant amount of extra space is used.
            
        
