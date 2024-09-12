class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        surplus, total_surplus = 0, 0
        start = 0
        for idx, (g, c) in enumerate(zip(gas, cost)):
            surplus += g - c
            total_surplus += g - c

            if surplus < 0:
                start = idx + 1
                # Reset surplus
                surplus = 0

        return start % len(gas) if total_surplus >= 0 else -1

"""
Time complexity: O(n)
Space complexity: O(1)
"""