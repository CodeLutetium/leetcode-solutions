class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        while low <= high:
            i = low + (high - low) // 2

            # Target found
            if nums[i] == target:
                return i

            # Target in first half of nums
            if nums[i] > target:
                high = i - 1
            # Target in second half of nums
            else:
                low = i + 1

        return -1
        
"""
Time complexity: O(log n)
Space complexity: O(1) (no additional space)
"""