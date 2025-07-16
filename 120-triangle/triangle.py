class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        curow = triangle[0]
        nxt = 2
        while nxt <=(len(triangle)):
            nextrow = [float('inf')]*nxt
            for i in range(nxt-1):
                nextrow[i] = min(nextrow[i],curow[i])
                nextrow[i+1] = min(nextrow[i+1],curow[i])
            for i in range(nxt):
                nextrow[i]+= triangle[nxt-1][i]
            curow = nextrow
            nxt+=1
        return min(curow)