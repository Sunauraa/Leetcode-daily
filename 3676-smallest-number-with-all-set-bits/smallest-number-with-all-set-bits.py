class Solution:
    def smallestNumber(self, n: int) -> int:
        cur = 2
        res = 1
        while res < n:
            res+=cur
            cur*=2
        return res