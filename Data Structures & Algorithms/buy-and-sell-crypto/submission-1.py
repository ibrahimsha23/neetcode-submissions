class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        purchased = prices[0]

        for price in prices:

            if price - purchased > profit:

                profit = max(price - purchased, profit)
            
            purchased = min(price, purchased)
        return profit


        