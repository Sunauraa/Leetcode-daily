class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10**9+7
        if not word:
            return 0
        
        groups = []
        count = 1
        for i in range(1, len(word)):
            if word[i]== word[i-1]:
                count+=1
            else:
                groups.append(count)
                count = 1
        groups.append(count)

        total = 1
        for g in groups:
            total = total*g%mod

        if k <= len(groups):
            return total
            
        dp = [0]*k
        dp[0] = 1
        
        for g in groups:
            new_dp = [0]*k
            sm = 0
            for s in range(k):
                if s > 0:
                    sm = (sm + dp[s-1])%mod
                if s > g:
                    sm = (sm - dp[s-g-1])%mod
                new_dp[s] = sm
            dp = new_dp
        invalid = sum(dp[len(groups):])%mod
        return(total - invalid)%mod