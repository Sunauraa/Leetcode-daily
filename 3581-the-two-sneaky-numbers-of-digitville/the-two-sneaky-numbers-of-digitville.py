class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        m = defaultdict(int)
        res = []
        for i in nums:
            m[i]+=1
            if m[i] >= 2:
                res.append(i)
        return res