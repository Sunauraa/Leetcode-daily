class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        cur = 1
        dp = []
        for i in range(32):
            if n&(1<<i):
                cur*=(1<<i)
                dp.append(cur)
                n-=(1<<i)
        MOD = 10**9+7
        res = []
        for l,r in queries:
            temp = dp[r]
            if l != 0:
                temp//=dp[l-1]
            res.append(temp%MOD)
        return res
            