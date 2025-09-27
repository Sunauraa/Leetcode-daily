class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        ans = 0
        #print(sqrt(4+4)/2)

        def length(fi,se):
            return sqrt( (fi[0] - se[0])**2 + (fi[1] - se[1])**2 )
        
        def area( x,y,z ):
            u = [ z[0] - x[0], z[1] - x[1] ]
            v = [ y[0] - x[0], y[1] - x[1] ]
            return float( sqrt( (u[0]*v[1] - u[1]*v[0])**2 )/2 )
        
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    u,v,w = length(points[i],points[j]), length(points[i],points[k]) , length(points[j],points[k])
                    if u + v >= w and u + w >= v and v + w >= u:
                        ans = max(ans, area(points[i],points[j],points[k]))
        return ans