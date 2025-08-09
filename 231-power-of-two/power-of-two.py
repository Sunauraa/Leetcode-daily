class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        @cache
        def multi ( x, p):
            if p == 0:
                return 1
            if p == 1:
                return x
            if p%2:
                return x*multi(x,p-1)
            temp = multi(x,p//2)
            return temp*temp
        
        l,r = 0,31
        ans = 0
        while l <= r:
            mid = (l+r)//2
            #print(mid,multi(2,mid))
            if multi(2,mid) == n:
                return True
            elif multi(2,mid) > n:
                r = mid -1
            else:
                ans = mid
                l = mid + 1
        #print(ans)
        return multi(2,ans) == n