class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n = str(n)
        m = defaultdict(int)
        for i in n:
            m[i]+=1
        temp = 1
        found = False
        for i in range(32):
            cur = str(temp)
            store = m.copy()
            for x in cur:
                store[x]-=1
            found =  all( x == 0 for x in store.values() )
            if found:
                return found
            temp*=2
        
        return found
            
                    