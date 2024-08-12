# Approach:
# The problem requires finding the diameter of a binary tree. The diameter is defined as the length of the longest path between any two nodes in the tree.
# This path may or may not pass through the root. The approach used here is a depth-first search (DFS) to calculate the height of the tree while keeping track of the maximum diameter found.

# Time Complexity: O(n), where n is the number of nodes in the tree.
# Each node is visited once, making the time complexity linear with respect to the number of nodes.

# Space Complexity: O(h), where h is the height of the tree.
# The space complexity is determined by the recursion stack, which, in the worst case, corresponds to the height of the tree.

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize the result as a list to store the maximum diameter found during DFS.
        res = [0]

        # Helper function to perform DFS on the tree.
        def dfs(root):
            # Base case: If the current node is None, return -1 (indicating no height).
            if not root:
                return -1

            # Recursively calculate the height of the left and right subtrees.
            left = dfs(root.left)
            right = dfs(root.right)

            # Update the maximum diameter found so far.
            # The diameter at the current node is the sum of the heights of the left and right subtrees plus 2.
            res[0] = max(res[0], 2 + left + right)

            # Return the height of the current node, which is 1 plus the maximum height of its left and right subtrees.
            return 1 + max(left, right)

        # Start the DFS from the root.
        dfs(root)

        # Return the maximum diameter found.
        return res[0]