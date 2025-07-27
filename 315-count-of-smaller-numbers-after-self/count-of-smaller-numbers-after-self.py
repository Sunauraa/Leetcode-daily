class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        store = []
        for i in range(n-1,-1,-1):
            ans[i] = bisect.bisect_left(store,nums[i])
            insort(store,nums[i])
        return ans