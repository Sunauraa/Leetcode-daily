class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowel = 'aeiou'
        cnt = 0
        for char in s:
            cnt += char in vowel
        return cnt > 0