class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[0])
        cnt = 0
        r = points[0][1]
        for i in points:
            if r >= i[0]:
                r = min(r,i[1])
            else:
                cnt+=1
                r = i[1]
            #print(l,r)
        return cnt+1

        