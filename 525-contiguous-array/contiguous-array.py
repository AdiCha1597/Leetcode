class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Initialize a hash table to store the first occurrence of each prefix sum
        prefix_sum_index = {0: -1}  # To handle the case when the subarray starts from index 0
        max_length = 0  # Variable to store the maximum length of the subarray
        prefix_sum = 0  # Variable to store the current prefix sum

        # Iterate over the array
        for i, num in enumerate(nums):
            # Update the prefix sum: +1 for 1, -1 for 0
            prefix_sum += 1 if num == 1 else -1

            # If the prefix sum has been seen before, it means there is a subarray with equal 0s and 1s
            if prefix_sum in prefix_sum_index:
                # Calculate the length of the subarray and update the max_length if it's longer than the previous one
                max_length = max(max_length, i - prefix_sum_index[prefix_sum])
            else:
                # If the prefix sum is seen for the first time, store its index
                prefix_sum_index[prefix_sum] = i

        return max_length

    '''
    # Approach:
        # 1. Use a hash table to store the first occurrence of each prefix sum.
        # 2. Traverse the array, updating the prefix sum: +1 for 1 and -1 for 0.
        # 3. Check if the current prefix sum has been seen before to calculate the subarray length.
        # 4. Update the maximum length if a longer subarray is found.
        Time: O(n) as we iterate the array once.
        Space: O(n): In the worst case, we might store all the prefix sums in the hash table.
    '''




        