class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordset=set(wordList)
        if endWord not in wordset:
            return 0

        q=deque()
        q.append([beginWord,1])
        visited=set()
        visited.add(beginWord)

        while q:
            currentword,step=q.popleft()
            if currentword==endWord:
                return step
            for i in range(len(currentword)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    new_word=currentword[:i]+char+currentword[i+1:]
                    if new_word in wordset and new_word not in visited:
                        visited.add(new_word)
                        q.append([new_word,step+1])
        return 0





        
        