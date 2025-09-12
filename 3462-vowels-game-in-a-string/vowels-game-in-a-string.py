class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return bool(s.count('a') or s.count('u') or s.count('i') or s.count('e') or s.count('o'))