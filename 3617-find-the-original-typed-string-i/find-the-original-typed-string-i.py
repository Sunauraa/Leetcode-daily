class Solution:
    def possibleStringCount(self, word: str) -> int:
        return sum( word[i] == word[i+1] for i in range(len(word)-1) ) + 1