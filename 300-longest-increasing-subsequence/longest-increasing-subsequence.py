class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 1
        n = len(nums)
        arr = [1]*n
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    arr[i] = max(arr[i], arr[j]+1)
                    ans = max(ans,arr[i])
        return ans