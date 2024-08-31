class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Generate combination sums
        combinations = []

        def make_combination(curr_sum, combination, idx):
            # Current sum meets target
            if curr_sum == target:
                combinations.append(combination.copy())
                return

            # Current sum exceeds target/ no valid indexes left: invalid combination, return
            if curr_sum > target or idx >= len(candidates):
                return

            # Add the same element
            combination.append(candidates[idx])
            make_combination(curr_sum + candidates[idx], combination, idx)

            # Add the next element
            combination.pop()
            make_combination(curr_sum, combination, idx+1)

        make_combination(0, [], 0)
        return combinations
    
"""
Time complexity: O(2^n)
"""