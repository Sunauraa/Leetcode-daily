class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        nums = nums + nums
        sm = 0
        n = len(nums)
        for i in range(n//2):
            sm+=nums[i]
        arr = [0]*n
        res = 0
        res += (n//2)*(target//sm)
        target%=sm
        l = -1
        r = 0
        ans = float('inf')
        temp = 0
        r = 0
        for l in range(n):
            while r < n and temp < target:
                temp += nums[r]
                r+=1
            if temp == target:
                ans = min(ans, r - l)
            temp-= nums[l]
        if ans == float('inf'):
            return -1
        else:
            return ans + res