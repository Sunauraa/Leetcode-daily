class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            s = s[::-1]
            x,y = y,x

        ans = 0
        cnta = 0
        cntb = 0
        for i in s:
            if i == 'a':
                cnta+=1
            elif i == 'b':
                if cnta > 0:
                    cnta-=1
                    ans+=x
                else:
                    cntb+=1
            else:
                ans += min(cnta,cntb)*y
                cnta = cntb = 0
        ans += min(cnta,cntb)*y
        return ans