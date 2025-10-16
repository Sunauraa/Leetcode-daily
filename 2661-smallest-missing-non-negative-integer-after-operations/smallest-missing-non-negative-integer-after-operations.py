class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        check = set()
        cur = [i for i in range(value)]
        for i in nums:
            check.add(cur[i%value])
            cur[i%value]+=value
        i = 0
        while i in check:
            i+=1
        return i