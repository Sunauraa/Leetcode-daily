class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        cur = 0
        res = 0
        for i in target:
            if cur < i:
                res+= i-cur
            cur = i
        return res