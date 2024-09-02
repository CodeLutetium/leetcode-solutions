class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        if len(nums) < 3:
            return max(nums)

        # dp array stores max profit at house i
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            # Max profit = max(house before, 2 house before + curr)
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]
    
"""
Time complexity: O(n)
Space complexity: O(n)
"""