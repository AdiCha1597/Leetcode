# Brute Force Approach:
# For each number in the array, check every other number to see if the two sum up to the target.
# Return the indices of the two numbers when a match is found.
# Time Complexity: O(n^2) as we are checking every possible pair.
# Space Complexity: O(1) as we do not use any additional data structures.

# Optimized Approach:
# Use a hash map (dictionary) to store each number and its index as we iterate through the list.
# For each number, check if the complement (target - current number) exists in the hash map.
# If it does, we have found the two numbers that add up to the target; return their indices.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # Dictionary to store number and its index

        for i, num in enumerate(nums):  # Iterate through the list
            complement = target - num  # Calculate the complement
            if complement in hashmap:  # Check if complement is already in the dictionary
                return [hashmap[complement], i]  # Return indices of the two numbers
            hashmap[num] = i  # Add the current number and its index to the dictionary

# Time Complexity: O(n), where n is the length of the nums list, as we only traverse the list once.
# Space Complexity: O(n) because we store each number in the hash map.