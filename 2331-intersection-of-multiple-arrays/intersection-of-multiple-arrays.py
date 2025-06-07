class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = []
        for i in nums[0]:
            if all(i in x for x in nums ):
                ans.append(i)
        ans.sort()
        return ans