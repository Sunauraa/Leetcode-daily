class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n = str(n)
        n=sorted(n)
        temp = 1
        found = False
        for i in range(32):
            cur = sorted(str(temp))
            found =  (cur==n)
            if found:
                return found
            temp*=2
        
        return found
            
                    