class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        """
            0: max length
            1: total possible subsequence
        """
        dp = [[0]*2 for _ in range(n)]
        mx = 0
        finmx = 0
        for i in range(n):
            mx = 0
            for j in range(0,i):
                if nums[i] > nums[j]:
                    mx = max(mx,dp[j][0])
            for j in range(0,i):
                if nums[i] > nums[j] and mx == dp[j][0]:
                    dp[i][1]+=dp[j][1]
            dp[i][0] = mx+1
            if not mx:
                dp[i][1] = 1
            finmx = max(finmx,dp[i][0])
        #print(dp)
        #print(mx)
        ans = 0
        for x,y in dp:
            if x == finmx:
                ans+=y
        return ans