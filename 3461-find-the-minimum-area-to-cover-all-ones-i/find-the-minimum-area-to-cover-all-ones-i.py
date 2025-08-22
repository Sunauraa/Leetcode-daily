class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        mnx,mxx,mny,mxy = inf,-inf,inf,-inf
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    mnx = min(mnx,i)
                    mxx = max(mxx,i)
                    mxy = max(mxy,j)
                    mny = min(mny,j)
        #print(mxx,mnx,mxy,mny)
        return (mxx-mnx+1)*(mxy-mny+1)