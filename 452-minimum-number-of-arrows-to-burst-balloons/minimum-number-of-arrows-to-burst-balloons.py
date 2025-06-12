class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        temp = set()
        for i in points:
            temp.add( (i[0],i[1]) )
        points = list(sorted(temp))
        #print(points)
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

        