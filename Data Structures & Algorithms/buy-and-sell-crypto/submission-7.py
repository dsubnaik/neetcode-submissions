class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit=0
        lowest_day=101
        for i in range(len(prices)):
            
            if prices[i]<lowest_day:
                lowest_day=prices[i]
                
            profit=prices[i]-lowest_day
            if profit > max_profit:
                max_profit = profit
                
        return max_profit