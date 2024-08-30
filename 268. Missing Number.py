class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = set([n for n in range(len(nums) + 1)])
        for num in nums:
            numbers.remove(num)
        return numbers.pop()