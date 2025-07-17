class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        ans = 0
        dp = [ [0]*k for _ in range(k)]
        for v,q in product(nums, range(k)):
                dp[q][v%k] = dp[q][ (k-v%k+q)%k ] + 1
                ans = max(ans, dp[q][v%k])
                #print(dp)
        return ans
        