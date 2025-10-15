class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        res = []
        cnt = 0
        cur = -inf
        for num in nums:
            if cur < num:
                cnt+=1
                cur = num
            else:
                res.append(cnt)
                cnt = 1
                cur = num
        res.append(cnt)
        #print(res)
        ans = 0
        for i in range(len(res)-1):
            ans = max(ans,min(res[i], res[i+1]),res[i]//2)
        ans = max(ans,res[-1]//2)
        return ans