class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pref = 0
        surf = 0
        ans = nums[0]
        for p,s in zip(nums,nums[::-1]):
            pref = p*(1 if pref == 0 else pref)
            surf = s*(1 if surf == 0 else surf)
            ans = max(ans,pref,surf)
            print(pref,surf,ans)
        return ans