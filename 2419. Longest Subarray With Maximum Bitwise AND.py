class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # AND of any two numbers will always result in a number <= original number
        max_value = 0
        res = 0
        curr_max = 0

        for num in nums:
            # Number larger than max_val
            if num > max_value:
                max_value = num
                curr_max = 1
                res = 1
            elif num == max_value:
                curr_max += 1
                res = max(res, curr_max)
            else:
                curr_max = 0

        return res

"""
Time complexity: O(n)
Space complexity: O(1)
"""