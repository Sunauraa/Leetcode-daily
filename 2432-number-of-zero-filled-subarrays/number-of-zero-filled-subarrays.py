class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        j = 0
        n = len(nums)
        for i in range(n):
            if j < i:
                j = i
            while j < n and nums[j] == 0:
                j+=1
            ans += j - i
        return ans