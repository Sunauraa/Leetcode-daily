class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(31,-1,-1):
            if n >= (1<<i):
                n-= (1<<i)
                res += ( 1<<(31-i) )
        return res
