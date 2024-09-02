class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        def max_profit(nums) -> int:
            profit = [0] * len(nums)
            profit[0] = nums[0]
            profit[1] = max(nums[0], nums[1])

            for i, num in enumerate(nums):
                if i < 2:
                    continue

                profit[i] = max(profit[i-1], profit[i-2] + num)

            return profit[-1]

        return max(max_profit(nums[1:]), max_profit(nums[:-1]))
    
"""
Time complexity: O(n)
Space complexity: O(n)
"""