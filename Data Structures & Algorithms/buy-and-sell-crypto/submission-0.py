class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        for i in range(n-1, 0, -1):
            temp_profit = prices[i] - min(prices[0:i])
            profit = max(temp_profit, profit)
        return profit