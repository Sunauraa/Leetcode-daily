class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        store = SortedList()
        for i in range(n-1,-1,-1):
            ans[i] = store.bisect_left(nums[i])
            store.add(nums[i])
        return ans