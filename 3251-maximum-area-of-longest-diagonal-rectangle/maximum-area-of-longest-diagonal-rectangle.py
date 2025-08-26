class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = 0
        curdiag = 0
        for l,r in dimensions:
            if sqrt(l*l + r*r) == curdiag:
                ans = max(ans,l*r)
            elif sqrt(l*l +r*r) > curdiag:
                curdiag = sqrt(l*l+r*r)
                ans = l*r
        return ans