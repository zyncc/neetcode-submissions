class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i, num in enumerate(prices):
            left, right = i + 1, len(prices) - 1

            while left <= right:
                profit = max(profit, prices[left] - num)
                left += 1

        return profit