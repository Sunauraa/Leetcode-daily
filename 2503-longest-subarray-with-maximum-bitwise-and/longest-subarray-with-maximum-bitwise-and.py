class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)
        i = 0 
        j = 0
        n = len(nums)
        ans = 1
        while i < n:
            if nums[i] != mx:
                i+=1
                continue
            j = i
            while j < n and nums[j] == mx:
                j+=1
            ans = max(ans,j-i)
            i = j
        return ans