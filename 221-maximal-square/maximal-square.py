class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        sm = [ [0]*m for _ in range(n) ]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    sm[i][j] = 1*(matrix[i][j] == '1')
                elif i == 0:
                    sm[i][j] += sm[i][j-1] + (matrix[i][j] == '1')
                elif j == 0:
                    sm[i][j] += sm[i-1][j] + (matrix[i][j] == '1')
                else:
                    sm[i][j] = sm[i-1][j] + sm[i][j-1] - sm[i-1][j-1] + (matrix[i][j] == '1')
        
        #print(sm)
        ans = 0
        for l in range(min(n,m), 0,-1):
            for i in range( l - 1 , n ):
                for j in range(l-1, m):
                    temp = sm[i][j]
                    if i - l != -1:
                        temp -= sm[i-l][j]
                    if j - l != -1:
                        temp -= sm[i][j-l]
                    if i - l != -1 and j - l != -1:
                        temp += sm[i-l][j-l]
                    if l*l == temp:
                        return l*l
        return ans