# https://leetcode.com/problems/contains-duplicate/
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Convert to set and compare lengths
        return len(set(nums)) != len(nums)

"""
Time complexity: O(n)
Space complexity: O(n)
"""
# Model solution from neetcode: 
# class Solution(object):
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hashset = set()

#         for n in nums: 
#             if n in hashset: 
#                 return True
#             hashset.add(n)
#         return False