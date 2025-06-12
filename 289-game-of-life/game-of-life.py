class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        rows = [-1,-1,-1,0,1,1,1,0]
        cols = [-1,0,1,1,1,0,-1,-1]
        for i in range(n):
            for j in range(m):
                board[i][j] += 2 + board[i][j]*2

        for i in range(n):
            for j in range(m):
                count = 0
                for k in range(8):
                    x,y = i - rows[k], j - cols[k]
                    if x >= 0 and x < n and y >= 0 and y < m:
                        count += ( board[x][y] >= 4 )
                if board[i][j] >= 5:
                    if count < 2:
                        board[i][j] = 4
                    elif count < 4:
                        board[i][j] = 5
                    else:
                        board[i][j] = 4
                elif count == 3:
                    board[i][j] = 3
        for i in range(n):
            for j in range(m):
                board[i][j] = 1*(board[i][j] == 3 or board[i][j] == 5)
        
                    
        