class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Get freq of all words occurence
        s1 = Counter(s1.split())
        s2 = Counter(s2.split())

        res = []

        # Loop through s1 first, delete from s2 if common word (for efficiency)
        for word, freq in s1.copy().items():
            # Common word: delete from both dicts
            if freq > 1:
                s1.pop(word, None)
                s2.pop(word, None)
            else:
                # Check if common in s2
                if s2.get(word, 0) == 0:
                    res.append(word)
                else:
                    s1.pop(word, None)
                    s2.pop(word, None)

        # Loop through remaining words in s2:
        for word, freq in s2.items():
            if freq == 1:
                res.append(word)

        return res

