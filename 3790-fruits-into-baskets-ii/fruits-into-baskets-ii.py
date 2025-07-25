class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        segs = [0]*(n*4+2)
        def build(id,l,r):
            if l == r:
                segs[id] = baskets[l]
                return
            mid = (l+r)//2
            build(id*2,l, mid)
            build(id*2+1, mid+1 , r)
            segs[id] = max(segs[id*2],segs[id*2+1])
        
        build(1,0,n-1)

        def take(id,l,r,val):
            if segs[id] < val:
                return False
            if l == r:
                if segs[id] >= val:
                    segs[id] = -inf
                    return True
                else:
                    return False
            mid = (l+r)//2
            ans = take(id*2,l,mid,val) or take(id*2+1,mid+1,r,val)
            segs[id] = max(segs[id*2],segs[id*2+1])
            return ans
        
        cnt = 0
        for i in fruits:
            check = take(1,0,n-1,i)
            #print(i,check)
            if not check:
                cnt+=1
        return cnt