class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        buy = 0
        for i in range(len(prices)):
            profit = prices[i] - prices[buy]
            max_p = max(max_p, profit)
            if prices[i] < prices[buy]:
                buy = i
        return max_p