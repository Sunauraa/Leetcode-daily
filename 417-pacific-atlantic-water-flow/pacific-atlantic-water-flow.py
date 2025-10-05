class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        Pacificvisit = [[0]*m for _ in range(n)]
        Atlanticvisit = [[0]*m for _ in range(n)]

        d = [[0,1],[1,0],[-1,0],[0,-1]]

        def visit( ocean, x,y):
            ocean[x][y] = 1
            for k in range(4):
                u = x + d[k][0]
                v = y + d[k][1]
                if 0 <= u < n and 0 <= v < m and not ocean[u][v] and heights[u][v] >= heights[x][y]:
                    visit(ocean,u,v)

        for i in range(n):
            visit( Pacificvisit, i ,0)
            visit( Atlanticvisit, i, m-1 )

        for j in range(m):
            visit( Pacificvisit, 0, j )
            visit( Atlanticvisit, n-1 , j)

        ans = []
        for i in range(n):
            for j in range(m):
                if Pacificvisit[i][j] and Atlanticvisit[i][j]:
                    ans.append( [i,j] )
        
        return ans