"""
208. Implement Trie (Prefix Tree): https://leetcode.com/problems/implement-trie-prefix-tree/description/
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        word = list(word)
        current = self.root
        while len(word) != 0 and (word[0] in current.children):
            current = current.children[word[0]]
            word = word[1:]
        if len(word) == 0 and current.terminal == True:
            return "Word already present."
        while len(word) != 0:
            current.children[word[0]] = TrieNode()
            current = current.children[word[0]]
            word = word[1:]
        current.terminal = True
        return "Word inserted sucessfully."

    def search(self, word: str) -> bool:
        word = list(word)
        current = self.root
        while len(word) != 0 and (word[0] in current.children):
            current = current.children[word[0]]
            word = word[1:]
        if len(word) == 0 and current.terminal == True:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        word = list(prefix)
        current = self.root
        while len(word) != 0 and (word[0] in current.children):
            current = current.children[word[0]]
            word = word[1:]
        if len(word) == 0:
            return True
        return False

myTrie = Trie()
print(myTrie.insert("apple"))
print(myTrie.insert("apple"))
print(myTrie.insert("apples"))
print(myTrie.search("apple"))
print(myTrie.startsWith("app"))

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)