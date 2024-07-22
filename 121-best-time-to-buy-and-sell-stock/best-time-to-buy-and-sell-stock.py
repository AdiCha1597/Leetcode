from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # Initialize pointers
        max_pro = 0  # Initialize max profit

        while r < len(prices):
            if prices[l] < prices[r]:  # Check if current profit is positive
                max_pro = max(prices[r] - prices[l], max_pro)  # Update max profit
            else:
                l = r  # Move left pointer to right pointer
            r += 1  # Move right pointer

        return max_pro  # Return the maximum profit

# Time Complexity: O(n)
# Space Complexity: O(1)

                    