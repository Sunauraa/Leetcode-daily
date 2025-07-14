class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        store = set()
        ans = 0
        for i in nums:
            if i not in store:
                store.add(i)
                ans+=i
            else:
                ans-=i
        return ans