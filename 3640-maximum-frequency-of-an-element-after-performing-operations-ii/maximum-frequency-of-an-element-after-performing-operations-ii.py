class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        freq = defaultdict(int)
        m = defaultdict(int)
        M = max(nums) + 2
        for num in nums:
            freq[num]+=1
            s,t = max(0, num - k), min(M, num+k+1)
            m[s]+=1
            m[t]-=1
        
        key = list(m.keys())
        key.sort()
        n = len(key)
        cur = 0
        cnt = m[key[0]]
        ans = max(freq.values())
        nums.sort()
        for num in nums:
            while cur < n - 1 and key[cur+1] <= num:
                ans = max(ans, min(numOperations,cnt ))
                cur+=1
                cnt+= m[key[cur]]
            ans = max(ans, min(numOperations+freq[num], cnt ))
        return ans