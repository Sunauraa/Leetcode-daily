class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        dp = []
        n = len(nums)
        i = 0
        while i < n:
            j = i+1
            temp = 1
            while j < n and nums[j] == nums[j-1]:
                j+=1
                temp+=1
            i = j
            dp.append(temp)
        cur = nums[0]
        ans = 0
        n = len(dp)
        check = True
        for i in range(n):
            if cur:
                ans = max(ans,dp[i])
            elif dp[i] == 1 and 0 < i < n - 1:
                ans = max(ans,dp[i-1] + dp[i+1])
                check = False
            else:
                check = False
            cur = not cur
        return ans - check