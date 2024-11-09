class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minB = prices[0]

        for i in prices:
            maxP = max(maxP,i - minB)
            if i < minB:
                minB = i
        
        return maxP
