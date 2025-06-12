class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()
        def nextnum( x ):
            temp = 0
            while x > 0:
                temp += (x%10)**2
                x//=10
            return temp
        while n not in check:
            check.add(n)
            n = nextnum(n)
            if n == 1:
                return True
        return False