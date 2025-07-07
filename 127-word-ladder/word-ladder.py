class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        queue = deque( [(beginWord,0)] )
        vi = set(beginWord)
        while queue:
            u,step = queue.popleft()
            vi.add(u)
            if u == endWord:
                return step + 1
            for i in range(len(beginWord)):
                for x in 'qwertyuiopasdfghjklzxcvbnm':
                    temp = u[:i] + x + u[i + 1:]
                    if temp in wordList and temp not in vi:
                        queue.append((temp, step+1))
        return 0