"""
211. Design Add and Search Words Data Structure
"""
class Word:
    def __init__(self):
        self.children = {}
        self.terminal = False

class WordDictionary:

    def __init__(self):
        self.root = Word()

    def addWord(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = Word()
            current = current.children[letter]
        current.terminal = True
        return None

    def search(self, word: str) -> bool:
        
        def recursiveSearch(root, string):
            current = root
            while len(string) != 0:
                if string[0] == '.':
                    for child_subtree in current.children.values():
                        if recursiveSearch(child_subtree, string[1:]):
                            return True
                elif string[0] not in current.children:
                    return False
                current = current.children[string[0]]
                string = string[1:]
            return True
        
        current = self.root
        string = word
        while len(string) != 0:
            if string[0] == '.':
                for child_subtree in current.children.values():
                    if recursiveSearch(child_subtree, string[1:]):
                        return True
            elif string[0] not in current.children:
                return False
            current = current.children[string[0]]
            string = string[1:]
        return True
    
myDictionary = WordDictionary()
myDictionary.addWord('bad')
myDictionary.addWord('mad')
myDictionary.addWord('sad')
myDictionary.addWord('tad')
print(myDictionary.search('..d'))

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)