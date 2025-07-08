class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isLeaf = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isLeaf = True   

    def search(self, word: str) -> bool:
        def dfs(curr,word):
            if not curr:
                return
            if curr.isLeaf and not word:
                return True
            for i in range(len(word)):
                if word[i] != '.':
                    index = ord(word[i]) - ord('a')
                    if not curr.children[index]:
                        return False
                    curr = curr.children[index]
                else:
                    for x in curr.children:
                        if x:
                            if dfs(x, word[i+1:]):
                                return True
                    return False
            return curr.isLeaf
        curr = self.root
        return dfs(curr,word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)