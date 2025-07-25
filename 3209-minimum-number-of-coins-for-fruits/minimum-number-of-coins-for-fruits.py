class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[inf]*2 for _ in range(n)]
        dp[0][0] = prices[0]
        dp[0][1] = prices[0]
        if n > 1:
            dp[1][1] = prices[0]
        for i in range(1,n):
            dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + prices[i]
            for x in range(i+1, min(n,i*2+2)):
                dp[x][1] = min(dp[x][1],dp[i][0])
            #print(dp[i][0],dp[i][1])
        return(min(dp[n-1][0],dp[n-1][1]))