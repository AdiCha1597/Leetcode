class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize the result counter and a hash map to store cumulative sums and their frequencies
        res = 0
        pre = {0: 1}  # Hash map to store the sum frequencies, initialized with sum 0 appearing once.
        add = 0  # This will store the cumulative sum of elements as we iterate through the list.

        for n in nums:
            add += n  # Update the cumulative sum with the current number
            diff = add - k  # Compute the difference needed to reach sum k

            res += pre.get(diff, 0)  # If diff exists in pre, it means there's a subarray that sums to k
            # Update the hash map with the new cumulative sum, incrementing the count of this sum
            pre[add] = 1 + pre.get(add, 0)

        return res  # Return the total count of subarrays that sum to k

# Time and Space Complexity:
# Time Complexity: O(n), where n is the length of nums. We make a single pass through the list.
# Space Complexity: O(n), where n is the number of unique cumulative sums stored in the hash map.


        