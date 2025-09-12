class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowel = 'aeiou'
        for char in s:
            if char in vowel:
                return True
        return False