class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = 0
        mn = nums[0]
        for i in range(1,len(nums)):
            ans = max(ans,nums[i]-mn)
            mn = min(mn,nums[i])
        return ans + -1*(ans==0)