class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Convert to lowercase, remove non alphanumeric
        letters = [letter.lower() for letter in s if letter.isalnum()]
        s = "".join(letters)

        start = 0
        end = len(s) - 1

        while(start < end):
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True

"""
Time complexity: O(n)
Space complexity: O(n) --> Can be improved to O(1) by not using extra array
"""
# Model leetcode ans
# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s)
#         reverse = cleaned_string[::-1]
#         if cleaned_string.lower() == reverse.lower():
#             return True
#         return False