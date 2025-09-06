class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        store = SortedList()
        n = len(nums)
        for j in range(k-1):
            store.add(nums[j])
        for i in range(k-1,n):
            store.add(nums[i])
            res.append(store[-1])
            store.remove(nums[i-k+1])
        return res
        