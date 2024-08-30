class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        set_bits = 0
        for digit in binary:
            if digit == "1":
                set_bits += 1

        return set_bits