class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_dict = {}
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
        
        freq_list = list(num_dict.values())
        freq_list.sort(reverse=True)
        top_freq = freq_list[:k]

        out = []
        for key in num_dict.keys():
            if num_dict[key] in top_freq:
                out.append(key)

        return out

"""
Time complexity: O(nlogn)
Space complexity: O(n)
"""

# Model solution:
# Time complexity: O(n) 
# Space complexity: O(n)
class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums: 
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res