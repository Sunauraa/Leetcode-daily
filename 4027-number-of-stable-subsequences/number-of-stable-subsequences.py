class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        dp = [ [[0]*2 for _ in range(2)] for __ in range(n) ]
        MOD = 10**9+7
        if n == 1:
            return 1
        for i in range(n):
            num = nums[i]
            state = num%2
            nonstate = not state
            dp[i][nonstate][0] += dp[i-1][nonstate][0]
            dp[i][nonstate][1] += dp[i-1][nonstate][1]
            dp[i][state][0] += dp[i-1][state][0]
            dp[i][state][1] += dp[i-1][state][1]
            #res+= dp[i][state][1]
            dp[i][state][0] += 1
            #print(dp[i][state][1])
            dp[i][state][1] += dp[i-1][state][0]
            dp[i][state][0] += dp[i-1][nonstate][1] + dp[i-1][nonstate][0]
            dp[i][nonstate][0] %=MOD
            dp[i][nonstate][1] %=MOD
            dp[i][state][0] %=MOD
            dp[i][state][1] %=MOD
            
        return (dp[n-1][0][1] + dp[n-1][0][0] + dp[n-1][1][0] + dp[n-1][1][1])%MOD