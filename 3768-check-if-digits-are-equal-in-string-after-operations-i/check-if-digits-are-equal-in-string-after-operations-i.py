class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            temp = ''
            n = len(s)
            for i in range(n-1):
                temp+=( str( (int(s[i])+int(s[i+1]))%10 ) )
            s = temp
        return s[0] == s[1]