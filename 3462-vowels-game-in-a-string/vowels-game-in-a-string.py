class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any( x in 'aeiou' for x in s)