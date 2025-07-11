class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        ans = float(inf)
        while l <= r:
            mid = (l+r)//2
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1
            ans = min(ans,nums[mid])
        return ans
