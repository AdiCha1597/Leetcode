# Approach:
# Use a greedy approach to capture all profitable transactions:
# - Iterate through the price list starting from the second day.
# - For each day, if the price is higher than the previous day's price, add the difference to the total profit.
# - This approach captures all upward movements, representing buying before a rise and selling after.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0  # Initialize total profit

        for i in range(1, len(prices)):  # Start from the second day
            # If today's price is higher than yesterday's, add the profit
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]  # Accumulate profit from positive differences

        return profit  # Return the total profit

# Time Complexity: O(n), where n is the length of the prices list, as we iterate through the list once.
# Space Complexity: O(1), as we only use a single variable to accumulate profit.