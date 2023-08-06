class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        L = 0
        for R in range(len(prices)):
            if prices[L] < prices[R]:
                maxProf = max(maxProf, prices[R]-prices[L])
            elif prices[L] > prices[R]:
                L = R 
        return maxProf
