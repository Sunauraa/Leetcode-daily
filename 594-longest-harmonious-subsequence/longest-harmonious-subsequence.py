class Solution:
    def findLHS(self, nums: List[int]) -> int:
        m = defaultdict(int)
        for i in nums:
            m[i]+=1
        v = sorted(list(m.keys()))
        ans = 0
        for i in range( len(v) - 1 ):
            if v[i] == v[i+1] - 1:
                ans = max(ans, abs(m[v[i]] + m[v[i+1]]))
        return ans

        