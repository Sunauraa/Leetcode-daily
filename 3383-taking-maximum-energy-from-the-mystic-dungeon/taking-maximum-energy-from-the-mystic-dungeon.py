class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0]*n
        for i in range(n):
            if i >= k:
                dp[i] = max(0,dp[i-k]) + energy[i]
            else:
                dp[i] = energy[i]
        #print(dp)
        return max(dp[n-k:])