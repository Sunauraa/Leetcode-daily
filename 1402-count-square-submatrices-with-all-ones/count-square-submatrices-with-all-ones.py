class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                elif matrix[i][j]:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                ans+=dp[i][j]
        #print(dp)
        return ans
