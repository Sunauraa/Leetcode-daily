class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 1
        n = len(points)
        if 1.0000000000000002 == 1:
            return 0
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
                #print(points[i],points[j],a,b)
                count = 2
                for o in range(j+1,n):
                    if a == float('inf'):
                        if points[o][0] == points[i][0]:
                            count+=1
                    elif round(a*(points[o][0]) + b,8) == points[o][1]:
                        #print(points[o])
                        count+=1
                    """if a == 3.0434782608695654 and b == 9.0:
                        print(points[o], a*(points[o][0]) + b,count)"""
                #print(count)
                ans = max(count,ans)
        return ans