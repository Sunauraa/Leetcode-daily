class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        col = [0,-1,0,1]
        row = [1,0,-1,0]
        n = len(board)
        m = len(board[0])
        vi = [[0]*m for i in range(n)]
        def region(x,y):
            vi[x][y] = 1
            nonlocal check
            if x == 0 or x == n - 1 or y == 0 or y == m - 1:
                check = 0
            for k in range(4):
                u = x + row[k]
                v = y + col[k]
                if 0 <= u < n and 0 <= v < m and board[u][v] == 'O' and not vi[u][v]:
                    region(u,v)
        
        def fill(x,y):
            board[x][y] = 'X'
            for k in range(4):
                u = x + row[k]
                v = y + col[k]
                if board[u][v] == 'O':
                    fill(u,v)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and not vi[i][j]:
                    check = 1
                    region(i,j)
                    if check:
                        fill(i,j)
        #print(vi)
     
        