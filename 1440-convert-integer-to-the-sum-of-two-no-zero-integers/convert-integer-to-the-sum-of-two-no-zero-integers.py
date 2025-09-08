class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def check( num ):
            while num > 0:
                if not num%10:
                    return False
                num//=10
            return True
        
        for i in range(1,n):
            if check(i) and check(n-i):
                return [i,n-i]