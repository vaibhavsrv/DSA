class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit = prices[0]
        max_profit = 0
        for i in prices[1:]:
            max_profit = max(max_profit,i - min_profit)
            min_profit = min(min_profit,i)
        return max_profit