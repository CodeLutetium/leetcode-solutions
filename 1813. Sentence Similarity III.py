class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Edge case: Both sentence are the same
        if sentence1 == sentence2:
            return True

        sentence1 = sentence1.split(" ")
        sentence2 = sentence2.split(" ")

        # Find longest common prefix (lcp)
        lcp = 0
        ceil = min(len(sentence1), len(sentence2))

        while lcp < ceil and sentence1[lcp] == sentence2[lcp]:
            lcp += 1

        # Find longest common suffix (lcs)
        lcs = 0
        
        while lcs < ceil and sentence1[len(sentence1) - 1 - lcs] == sentence2[len(sentence2) - 1 - lcs]:
            lcs += 1

        if len(sentence1) > 1 and len(sentence2) > 1:
            return lcp + lcs >= ceil
        else:
            return lcp > 0 or lcs > 0
        
"""
Time complexitY: O(n)
Space compleixty: O(1) (assuming splitting of string to arrays does not count as extra mem)
"""