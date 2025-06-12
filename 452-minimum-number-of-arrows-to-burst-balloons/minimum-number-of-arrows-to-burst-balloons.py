class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        temp = set()
        for i in points:
            temp.add( (i[0],i[1]) )
        points = list(sorted(temp))
        print(points)
        cnt = 0
        l,r = points[0]
        for i in points:
            if r >= i[0]:
                r = min(r,i[1])
                l = max(l,i[0])
            else:
                cnt+=1
                l,r = i
            #print(l,r)
        return cnt+1

        