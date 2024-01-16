class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = 0
        sell = 1
        profit = 0

        while sell < len(prices):
            # Check profit
            if prices[sell] > prices[buy]:
                profit = max(prices[sell] - prices[buy], profit)
            else:
                buy = sell

            sell += 1

        return profit
            
"""
Time complexity: O(n)
Space complexity: O(1)
"""