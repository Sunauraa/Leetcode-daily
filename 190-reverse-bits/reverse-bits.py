class Solution:
    def reverseBits(self, n: int) -> int:
        ans = ''
        while n > 0:
            ans = chr( n%2 + ord('0') ) + ans
            n//=2
        ans = '0'*(32 - len(ans)) + ans
        #ans = ans[::-1]
        cur = 1
        res = 0
        for i in ans:
            if i == '1':
                res+=cur
            cur*=2
        return res
