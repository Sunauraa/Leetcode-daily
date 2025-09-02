class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)
        for i in range(n):
            for j in range(n):
                if i == j or points[i][0] > points[j][0] or points[i][1] < points[j][1]:
                    continue
                check = True
                for o in range(n):
                    if o == i or o == j:
                        continue
                    if points[i][0] <= points[o][0] <= points[j][0] and points[i][1] >= points[o][1] >= points[j][1]:
                        #print( points[i], points[o], points[j] )
                        check = False
                        break
                ans+=check
        return ans