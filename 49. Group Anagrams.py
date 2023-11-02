# https://leetcode.com/problems/group-anagrams/
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)

        for string in strs:
            key = ''.join(sorted(string))
            groups[key].append(string)
        
        return list(groups.values())

"""
Time complexity: O(n)
Space complexity: O(n)
"""