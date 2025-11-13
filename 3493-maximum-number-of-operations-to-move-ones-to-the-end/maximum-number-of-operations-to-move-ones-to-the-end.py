class Solution:
    def maxOperations(self, s: str) -> int:
        cur = 0
        res = 0
        n = len(s)
        for i in range(n):
            if s[i] == "1":
                cur+=1
                if i < n - 1 and s[i+1] == "0":
                    res+= cur
        return res