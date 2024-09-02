class Trie:
    # Time complexity: O(1) 
    def __init__(self):
        self.root = defaultdict(dict)

    # Time complexity: O(n)
    # Space complexity: O(n)
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            # Create dict if encountering character for the first time
            if char not in curr.keys():
                curr[char] = defaultdict(dict)
            curr = curr[char]
        
        # Append terminating character
        curr["\0"] = True

    # Time complexity: O(n)
    # Space complexity: O(1) (no additional space used)
    def search(self, word: str) -> bool:
        curr = self.root
        
        for char in word:
            if char not in curr.keys():
                return False
            curr = curr[char]
        
        # Check for terminating character
        return curr["\0"]

    # Time complexity: O(n)
    # Space complexity: O(1) (no additional space used)
    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr.keys():
                return False
            curr = curr[char]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)