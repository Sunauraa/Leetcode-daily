class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        lwst = float('-inf')
        ans = lwst
        cur = lwst
        n = len(nums)
        lf = [0]*n
        rt = [0]*n
        for i in range( n ):
            if i == pos:
                break
            if cur == lwst:
                cur = nums[i]
            else:
                cur+= nums[i]
            ans = max(ans,cur)
            if cur < 0:
                cur = lwst
        for i in range(n):
            if i != 0:
                lf[i] = lf[i-1]
            lf[i]+=nums[i]
        for i in range( n-1, -1,-1 ):
            if i != n-1:
                rt[i] = rt[i+1]
            rt[i]+=nums[i]
        for i in range(1,n):
            lf[i] = max(lf[i], lf[i-1] )
        for i in range(n-2,-1,-1):
            rt[i] = max(rt[i], rt[i+1])
        for i in range( 1, n-1 ):
            ans = max( ans , lf[i] + rt[i+1] )
        return ans