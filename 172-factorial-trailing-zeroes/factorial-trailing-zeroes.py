class Solution:
    def trailingZeroes(self, n: int) -> int:
        temp = 0
        while n>=5:
            n//=5
            temp+=n
        return temp