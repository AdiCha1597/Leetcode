# Brute Force Approach:
# Check the profit for every possible pair of days by calculating the difference between each pair of prices.
# Keep track of the maximum profit observed during these comparisons.
# Time Complexity: O(n^2) because we compare each day with every other day.
# Space Complexity: O(1) since we only need a variable to track the maximum profit.

# Optimized Approach:
# Use two pointers (left and right) to track the minimum buying price and the potential selling price.
# Update the maximum profit whenever a higher profit is found, moving the pointers accordingly.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # Initialize pointers for buy and sell days
        max_pro = 0  # Initialize max profit

        while r < len(prices):  # Iterate until the right pointer reaches the end
            if prices[l] < prices[r]:  # Check if current profit is positive
                max_pro = max(prices[r] - prices[l], max_pro)  # Update max profit if the current profit is higher
            else:
                l = r  # Move left pointer to right pointer if buying price is higher than selling price
            r += 1  # Move right pointer to the next day

        return max_pro  # Return the maximum profit

# Time Complexity: O(n), where n is the length of the prices array, as we only traverse the list once.
# Space Complexity: O(1) because we only use a few extra variables.
