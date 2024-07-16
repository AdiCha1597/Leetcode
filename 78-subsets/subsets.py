class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []  # This will hold all subsets
        subset = []  # A temporary list to hold a single subset

        def helper(i):
            if i >= len(nums):  # Base case: if index reaches the end of list
                res.append(subset.copy())  # Append the copy of subset to results
                return
            
            # Include the current element and move to the next
            subset.append(nums[i])
            helper(i + 1)

            # Exclude the current element and move to the next
            subset.pop()
            helper(i + 1)

        helper(0)  # Initialize the recursive helper function
        return res

# Time Complexity: O(2^n) because each element has two choices (include or not include).
# Space Complexity: O(n) due to the recursion depth.
