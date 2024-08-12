# Approach:
# The problem requires inverting a binary tree, meaning we need to swap the left and right children of each node in the tree.
# The approach used here is a recursive one. For each node, we swap its left and right children and then recursively apply the same operation to each child.
# This process is repeated until the entire tree is inverted.

# Time Complexity: O(n) where n is the number of nodes in the tree.
# We visit each node exactly once, so the time complexity is linear with respect to the number of nodes.

# Space Complexity: O(h) where h is the height of the tree.
# The space complexity is determined by the recursion stack, which, in the worst case (for a skewed tree), is equal to the height of the tree.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: If the root is None, there's nothing to invert, so return None.
        if not root:
            return None

        # Swap the left and right children of the current node.
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # Recursively invert the left subtree.
        self.invertTree(root.left)
        
        # Recursively invert the right subtree.
        self.invertTree(root.right)

        # Return the root of the inverted tree.
        return root