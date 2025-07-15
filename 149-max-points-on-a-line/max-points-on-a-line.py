class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 1
        n = len(points)
        def linear(u,v):
            if u[1] - v[1] == 0:
                a = 0
            elif u[0] - v[0] == 0:
                a = float('inf')
            else:
                a = (u[1]-v[1])/(u[0]-v[0])
            b = u[1] - a*u[0]
            return a,b

        for i in range(n):
            for j in range(i+1,n):
                a,b = linear(points[i],points[j])
                count = 2
                for o in range(j+1,n):
                    if a == float('inf'):
                        if points[o][0] == points[i][0]:
                            count+=1
                    elif round(a*(points[o][0]) + b,8) == points[o][1]:
                        count+=1
                ans = max(count,ans)
        return ans