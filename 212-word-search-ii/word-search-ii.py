class TrieNode:
    def __init__(self):
        self.children = [0]*26

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        row = [1,0,-1,0]
        col = [0,-1,0,1]
        root = TrieNode()

        def insert(word):
            curr = root
            for c in word:
                index = ord(c) - ord('a')
                if not curr.children[index]:
                    curr.children[index] = TrieNode()
                curr = curr.children[index]
        store = set()

        n = len(board)
        m = len(board[0])
        def dfs( i , j , word):
            #print(word)
            #print(i,j)
            vi[i][j] = 1
            if word not in store:
                insert(word)
                store.add(word)
            if len(word) <= 9:
                for k in range(4):
                    x = i + row[k]
                    y = j + col[k]
                    if 0 <= x < n and 0 <= y < m and not vi[x][y]:
                        dfs(x,y,word + board[x][y])
            vi[i][j] = 0

        for i in range(n):
            for j in range(m):
                vi = [ [0]*m for _ in range(n) ]
                dfs(i,j,board[i][j])

        def check(word):
            curr = root
            for c in word:
                index = ord(c) - ord('a')
                if not curr.children[index]:
                    #print(c)
                    return False
                curr = curr.children[index]
            return True

        ans = []
        for x in words:
            #print(x)
            if check(x):
                ans.append(x)
        #print(root.children)
        return ans
            