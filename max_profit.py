'''
You are given an integer array prices where prices[i] is the price of 
a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only 
hold at most one share of the stock at any time. However, you can buy it 
then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
'''
class Solution:
    def maxProfit(self, prices: int) -> int:
        max_profit=0
        for i in range(len(prices)-1):
            if (prices[i+1]> prices[i]):
                max_profit += prices[i+1]-prices[i]
        return max_profit

        
        
                
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([1, 7, 2, 3, 6, 7, 6, 7]))