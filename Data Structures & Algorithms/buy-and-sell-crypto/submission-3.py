class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        p = 0
        lowest = float('inf')

        for i in prices:
            lowest = min(lowest, i)
            profit = max(profit, i - lowest)
            
        return profit
            



        