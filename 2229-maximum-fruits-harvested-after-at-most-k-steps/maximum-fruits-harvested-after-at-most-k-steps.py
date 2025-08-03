class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        dp = [(-1,0)]
        cur = 0
        for fruit in fruits:
            cur+= fruit[1]
            dp.append((fruit[0],cur))
        ans = 0

        def binsearch(k,fi,u,v):
            #print(k,fi,u,v)
            l = u
            r = v
            res = 0
            while l <= r:
                mid = (l + r)//2
                if min(startPos-fi,mid - startPos)*2 + max(startPos-fi,mid-startPos) <= k:
                    res = mid
                    l = mid + 1
                else:
                    r = mid -1
                #print(mid,l,r)
            return res

        #print(dp)
        for i in range(n):
            l = fruits[i]
            if l[0] < startPos - k or l[0] > startPos+k:
                continue
            mem = min(l[0]+k,startPos+k)
            if l[0] < startPos:
                mem = binsearch(k, l[0], startPos,startPos+k)
            pos = bisect.bisect_left(dp, (mem,inf))
            #print(l,pos)
            #print(dp)
            ans = max(ans,dp[pos-1][1]-dp[i][1])
        return ans