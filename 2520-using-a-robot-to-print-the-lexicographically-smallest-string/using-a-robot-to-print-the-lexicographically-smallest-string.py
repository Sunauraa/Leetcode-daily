class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        mn = [s[n-1]]*n
        for i in range(n-2 , -1 , -1):
            mn[i] = min(mn[i+1], s[i])
        t = []
        ans = ''
        for i in range(n):
            if s[i] == mn[i]:
               ans+=s[i]
            else:
                t.append(s[i])
            if i < n-1:
                while len(t) > 0 and t[len(t)-1] <=  mn[i+1]:
                    ans+= t[len(t)-1]
                    t.pop(len(t)-1)
        return ans + ''.join(t[::-1])

