class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        store = SortedList()
        ans = 0
        for i in range(n-1,-1,-1):
            #print(nums[i]//2-1)
            ans += store.bisect_left(nums[i]//2 + (nums[i]%2))
            store.add(nums[i])
            #print(ans,store)
        return ans