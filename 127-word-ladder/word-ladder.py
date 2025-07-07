class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque( [(beginWord,0)] )
        ans = float('inf')
        vi = defaultdict(int)

        def dif(u,v):
            count = 1
            for x,y in zip(u,v):
                if x != y:
                    count-=1
                    if count < 0:
                        return False
            return count == 0

        n = len(wordList)
        while queue:
            #print(queue)
            u,step = queue.popleft()
            if u == endWord:
                return step + 1
            temp = 0
            while temp < n:
                if dif(wordList[temp],u):
                    queue.append((wordList[temp], step+1))
                    wordList.remove(wordList[temp])
                    n-=1
                else:
                    temp+=1
        return 0
            