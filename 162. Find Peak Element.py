class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        start = 0
        end = len(nums) - 1

        while start <= end:
            # Early return
            if end - start == 1:
                return end if nums[end] > nums[start] else start

            mid = (start + end) // 2
            
            # Early return
            if mid == 0 and nums[0] > nums[1]:
                return 0

            if mid == (len(nums) - 1) and nums[-1] > nums[-2]:
                return mid

            # Return peak
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            # Shift to side of array with larger number
            if nums[mid + 1] > nums[mid]:
                start = mid + 1
            else: 
                end = mid - 1

        return -1

"""
Time complexity: O(log n) (binary search)
Space complexity: O(1) (O(log n) if using recursion)
"""