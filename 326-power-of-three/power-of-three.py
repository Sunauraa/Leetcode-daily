class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 0 and not n%3:
            n//=3
        return n==1