class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a>= 0 and b >= 0:
            while b > 0:
                carry = a&b
                a^=b
                b = carry << 1
            return a
        elif a < 0 and b < 0:
            a = abs(a)
            b = abs(b)
            while b > 0:
                carry = a&b
                a^=b
                b = carry << 1
            return -a
        elif (a >= 0 and b < 0) or (a < 0 and b >= 0):
            neg = False
            if (a < 0 and abs(a) > b) or (b < 0 and abs(b) > a):
                neg = True
            b = abs(b)
            a = abs(a)
            if a < b:
                a,b = b,a
            while b > 0:
                carry = (~a)&b
                a^=b
                b = carry << 1
            if neg:
                return -a
            return a