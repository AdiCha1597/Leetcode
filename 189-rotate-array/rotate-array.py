class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # k = k % n
        # res = [0] * n
        # for i in range(n):
        #     pos = (i + k) % n
        #     res[pos] = nums[i]
        
        # nums[:] = res
        # TC : O(n), SC: O(n)

        n = len(nums)
        k = k % n  # Adjust k to ensure it is not greater than n
        
        def helper(l, r):
            # Reverse elements from index l to r
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]  # Swap the elements at l and r
                l, r = l + 1, r - 1  # Move the pointers inward

        # Reverse the entire array
        helper(0, n - 1)
        # Reverse the first k elements (these will become the last k elements)
        helper(0, k - 1)
        # Reverse the rest of the array (the former last part)
        helper(k, n - 1)

# Time Complexity: O(n)
# Space Complexity: O(1)




