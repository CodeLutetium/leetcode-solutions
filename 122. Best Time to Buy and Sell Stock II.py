class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prev = prices[0]

        for price in prices:
            if price > prev:
                profit += price - prev
            prev = price

        return profit