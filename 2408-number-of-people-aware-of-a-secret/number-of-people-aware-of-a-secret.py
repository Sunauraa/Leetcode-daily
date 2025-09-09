class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        if delay == forget:
            return n < delay
        dp = [0]*n
        dp[0] = 1
        MOD = 10**9 + 7
        for i in range(n):
            if dp[i]:
                for j in range(i+delay,min(n,i+forget)):
                    dp[j]+=dp[i]
                    dp[i]%=MOD
        #print(dp)
        return sum(dp[n-forget:])%MOD