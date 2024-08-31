class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1

        while end >= start + 1:
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:   # min is in right half
                start = mid + 1
            else:
                end = mid
                 
        return nums[start]
"""
Time complexity: O(log n)
Space complexity: O(1)
"""