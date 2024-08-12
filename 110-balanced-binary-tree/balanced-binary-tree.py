# Approach:
# The problem is to determine whether a binary tree is height-balanced. 
# A binary tree is balanced if the depth of the two subtrees of every node never differs by more than one.
# This solution uses a bottom-up approach, where we perform a depth-first search (DFS) to determine both the height of the tree and whether it is balanced, starting from the leaf nodes and moving up to the root.

# Time Complexity: O(n), where n is the number of nodes in the tree.
# We visit each node exactly once to compute both its height and balanced status.

# Space Complexity: O(h), where h is the height of the tree.
# The space complexity is determined by the recursion stack, which, in the worst case,
# is equal to the height of the tree.

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function to perform DFS on the tree.
        def dfs(root):
            # Base case: If the current node is None, it is balanced, and its height is 0.
            if not root: 
                return [True, 0]

            # Recursively check the left and right subtrees.
            left, right = dfs(root.left), dfs(root.right)

            # A tree is balanced if both subtrees are balanced and the height difference between them is not more than 1.
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            # Return whether the tree is balanced and its height.
            return [balanced, 1 + max(left[1], right[1])]

        # Start the DFS from the root and return whether the entire tree is balanced.
        return dfs(root)[0]      
        

        