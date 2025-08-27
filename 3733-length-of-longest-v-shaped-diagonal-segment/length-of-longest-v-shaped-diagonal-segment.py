class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        direct = [[1,1],[1,-1],[-1,-1],[-1,1]]
        n,m = len(grid),len(grid[0])
        ans = 0

        @cache
        def dfs(i,j,d,turn,target):
            x,y = i + direct[d][0], j + direct[d][1]
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != target:
                return 0

            maxstep = dfs(x,y,d,turn, 2 - target)
            if turn:
                maxstep = max(maxstep, dfs(x,y,(d+1)%4,False,2 - target))
            
            return maxstep+1



        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for k in range(4):
                        ans = max(ans,dfs(i,j,k,1,2)+1)


        return ans