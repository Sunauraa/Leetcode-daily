class TrieNode:
    def __init__(self):
        self.children = [0]*27
        self.isLeaf = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key = lambda x: len(x))
    
        def buildTrie(x):
            cur = root
            for c in x:
                idx = ord(c) - ord('a')
                if c == '/':
                    idx = 26
                if not cur.children[idx]:
                    cur.children[idx] = TrieNode()
                cur = cur.children[idx]
            cur.isLeaf = True
        root = TrieNode()
        def checkTrie(x):
            cur = root
            res = ''
            check = False
            for c in x:
                if c == '/':
                    idx = 26
                else:
                    idx = ord(c) - ord('a')
                if cur.isLeaf and idx == 26:
                    check = True
                if not check:
                    res+=c
                else:
                    return res
                if not cur.children[idx]:
                    return res
                cur = cur.children[idx]
            return res

        ans = set()
        for fold in folder:
            buildTrie(fold)
            #print(checkTrie(fold))
            ans.add(checkTrie(fold))

        return list(ans)
            
