class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        left,right = 0,0
        for i in range(len(nums)):
            right = i
            if nums[right] - nums[left] > k:
                ans+=1
                left = i
        return ans + 1