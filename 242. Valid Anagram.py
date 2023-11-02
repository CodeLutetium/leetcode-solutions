# https://leetcode.com/problems/valid-anagram/
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Sort both strings and check if same
        return sorted(s) == sorted(t)

"""
Time complexity: O(nlogn), depends on sorting algorithm
Space complexity: O(1) to O(n), depending on sorting algorithm
"""