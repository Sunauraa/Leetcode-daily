class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        k = 1
        while True:
            num1-=num2
            if num1 < k: return -1
            if num1 >= 0 and k >= num1.bit_count():
                return k
            k+=1
        return -1