class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque( [(beginWord,0)] )
        ans = float('inf')
        wordList = set(wordList)
        vi = set()

        while queue:
            u,step = queue.popleft()
            vi.add(u)
            if u == endWord:
                return step + 1
            for i in range(len(beginWord)):
                for x in 'qwertyuiopasdfghjklzxcvbnm':
                    if u[i] == x:
                        continue
                    temp = u[:i] + x + u[i + 1:]
                    if temp in wordList and temp not in vi:
                        queue.append((temp, step+1))
        return 0