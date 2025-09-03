class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort( key = lambda x: (x[0], -x[1]), reverse = True )
        ans = 0
        n = len(points)
        for i in range(n):
            mny = inf
            mnx = points[i][0]
            #print(points[i],mny,mnx)
            for j in range(i+1,n):
                if points[j][0] <= mnx and points[j][1] < mny and points[j][1] >= points[i][1]:
                    ans+=1
                    mnx = min(mnx,points[j][0])
                    mny = min(mny,points[j][1])
        return ans