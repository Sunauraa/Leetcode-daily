class Solution:
    def maxSum(self, nums: List[int]) -> int:
        m = defaultdict(int)
        ans = 0
        if not any( i > 0 for i in nums):
            return max(nums)
        for r in nums:
            if r not in m and r > 0:
                ans+=r
                m[r]+=1
        return ans
