class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        segs = [0]*4*n
        def build(id,l,r):
            if l == r:
                segs[id] = baskets[l]
                return
            mid = (l+r)//2
            build(id*2, l, mid )
            build(id*2 +1, mid+1, r)
            segs[id] = max(segs[id*2],segs[id*2+1])
        build(1,0,n-1)

        def take(id,l,r,x):
            if segs[id] < x:
                return False
            if l == r:
                if segs[id] >= x:
                    segs[id] = -inf
                    return True
                return False
            mid = (l+r)//2
            check = take(id*2,l,mid,x) or take(id*2+1,mid+1,r,x)
            segs[id] = max(segs[id*2],segs[id*2+1])
            return check
        
        ans = 0
        for i in fruits:
            ans+= take(1,0,n-1,i)
        return n - ans