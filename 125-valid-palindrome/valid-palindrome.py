class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        s = s.lower()
        for i in s:
            if ( i >= 'a' and i <= 'z') or ( i >='0' and i <= '9'):
                res +=i
        if res == res[::-1]:
            return True
        else:
            return False
        