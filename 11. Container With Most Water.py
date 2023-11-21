class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            # Calculate area and update max_area
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)

            # Move pointer based on smaller height
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
    
"""
Time complexity: O(n)
Space complexity: O(1)
"""