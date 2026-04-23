class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #typical sliding window problem
        L,profit=0,0
        for R in range(len(prices)):
            # while prices[R]>prices[L]:
            #     profit=prices[R]-prices[L]
            if prices[R]>prices[L]:
                profit=max(profit, prices[R]-prices[L])
            else:
                # L+=1
                L=R
        return max(profit, 0)