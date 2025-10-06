class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = []
        d = [[1,0],[0,1],[0,-1],[-1,0]]
        dijk = [[inf]*m for _ in range(n)]
        vi = set((0,0))
        dijk[0][0] = grid[0][0]
        heapq.heappush( q, (dijk[0][0], 0,0) )
        while q:
            temp,u,v = heapq.heappop(q)
            if (u,v) in vi:
                continue
            vi.add((u,v))
            for k in range(4):
                nxu,nxv = u + d[k][0],v + d[k][1]
                if 0 <= nxu < n and 0 <= nxv < m and (nxu,nxv) not in vi:
                    dijk[nxu][nxv] = max(dijk[u][v], grid[nxu][nxv])
                    if nxu == n-1 and nxv == m-1:
                        return dijk[nxu][nxv]
                    heapq.heappush(q,(dijk[nxu][nxv], nxu,nxv))
        
        return dijk[n-1][m-1]