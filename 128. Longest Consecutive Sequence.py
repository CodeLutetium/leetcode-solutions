class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0

        # Set of all the numbers avail
        num_set = set(nums)

        for num in num_set:
            # Check if prev number in set. 
            # If not in set, potential to be start of longest subseq
            if num-1 not in num_set:
                length = 0
                # Check each subsequent num, see if in numset
                while num + length in num_set:
                    length += 1
                
                # Set longest to the max value
                longest = max(length, longest)
        return longest
        