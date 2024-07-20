from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        # Edge case: if the input list is empty, return an empty list
        if n == 0:
            return []
        # Edge case: if the input list has one element, return a list containing that element
        elif n == 1:
            return [nums]
        
        res = []  # This will store all the permutations

        # Helper function to perform DFS
        def dfs(subset):
            # If the subset's length equals n, we've formed a complete permutation
            if len(subset) == n:
                res.append(subset.copy())  # Add a copy of the subset to results

            # Iterate through all numbers in the input list
            for num in nums:
                # Only add the number to the subset if it is not already present
                if num not in subset:
                    subset.append(num)  # Add the number to the current subset
                    dfs(subset)  # Recursively call dfs with the updated subset
                    subset.pop()  # Backtrack by removing the last number added
        
        dfs([])  # Initial call to dfs with an empty subset
        return res

# Time Complexity: O(N * N!), where N is the number of elements in nums.
# The number of permutations of a list of N elements is N!, and creating each permutation takes O(N) time due to the copying of the subset.
# Space Complexity: O(N), for the recursion stack and the current subset being built.

        