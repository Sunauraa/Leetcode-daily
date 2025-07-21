class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [0]*n
        dp[0] = nums[0]
        ans1 = 0
        ans2 = 0
        for i in range(n-1):
            dp[i] = max(dp[i-1],dp[i-2] + nums[i])
            ans1 = max(ans1,dp[i])
        #print(dp)
        dp = [0]*n
        dp[1] = nums[1]
        for i in range(1,n):
            dp[i] = max(dp[i-1],dp[i-2] + nums[i])
            ans2 = max(ans2,dp[i])
        #print(dp)
        return max(ans1,ans2)