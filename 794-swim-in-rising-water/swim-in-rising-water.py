class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = []
        d = [[1,0],[0,1],[0,-1],[-1,0]]
        dijk = [[inf]*m for _ in range(n)]
        vi = [[0]*m for _ in range(n)]
        dijk[0][0] = grid[0][0]
        heapq.heappush( q, (dijk[0][0], 0,0) )
        while q:
            temp,u,v = heapq.heappop(q)
            if vi[u][v]:
                continue
            vi[u][v] = 1
            for k in range(4):
                nxu,nxv = u + d[k][0],v + d[k][1]
                if 0 <= nxu < n and 0 <= nxv < m and not vi[nxu][nxv]:
                    dijk[nxu][nxv] = max(dijk[u][v], grid[nxu][nxv])
                    heapq.heappush(q,(dijk[nxu][nxv], nxu,nxv))
        
        return dijk[n-1][m-1]