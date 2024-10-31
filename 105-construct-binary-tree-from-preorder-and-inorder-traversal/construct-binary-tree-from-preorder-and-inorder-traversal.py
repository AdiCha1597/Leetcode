# Approach:
# 1. The first element in the preorder list is the root of the tree.
# 2. Find the index of this root in the inorder list. Elements to the left of this index
#    are in the left subtree, and elements to the right are in the right subtree.
# 3. Recursively repeat the process to construct the left and right subtrees
#    using the corresponding elements in preorder and inorder lists.

from typing import List, Optional

#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:  # Base case: return None if either list is empty
            return None

        root = TreeNode(preorder[0])  # The first element of preorder is the root
        mid = inorder.index(preorder[0])  # Find root index in inorder to split left and right subtrees

        # Recursively build the left subtree with left side of inorder and corresponding preorder
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])

        # Recursively build the right subtree with right side of inorder and corresponding preorder
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root  # Return the constructed tree root node

# Time Complexity: O(n^2) in the worst case, as the index search in inorder requires O(n) and is done recursively.
# Space Complexity: O(n^2) due to recursive calls and array slicing, where each recursive call may create new subarrays.