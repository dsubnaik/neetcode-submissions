class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price=prices[i]
            
            if prices[i]-min_price>max_profit:
                max_profit=prices[i]-min_price
                
        return max_profit
array=[10,1,5,6,7,1]
sol=Solution()
print(sol.maxProfit(array))
        
        
        