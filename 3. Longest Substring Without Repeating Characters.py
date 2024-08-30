class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Edge cases
        if len(s) <= 1:
            return len(s)

        start = 0
        chars = set()
        longest = 1

        for end in range(len(s)):
            while s[end] in chars:
                chars.remove(s[start])
                start += 1

            chars.add(s[end])
            longest = max(longest, len(chars))
        return longest
                
                
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""