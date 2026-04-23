class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = float('inf')
        maxProfit = 0
        for i in prices: 
            if i < min_prices: min_prices = i
            else :
                profit = i - min_prices 
                maxProfit = max(profit, maxProfit)
        return maxProfit 