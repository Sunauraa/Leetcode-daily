class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cur = 0
        ns = len(s)
        if ns == 0:
            return True
        nt = len(t)
        for i in range(nt):
            if t[i] == s[cur]:
                cur+=1
                if cur == ns:
                    return True
        return False