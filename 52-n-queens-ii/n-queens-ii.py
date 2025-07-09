class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [ [1]*n for _ in range(n) ]
        ans = 0

        def fill( i,j,val ):
            for x in range(n):
                board[i][x]+=val
            for x in range(n):
                board[x][j] += val
            u,v = i,j
            while n > u >= 0 and n > v >= 0:
                board[u][v] += val
                u +=1
                v +=1
            
            u,v = i,j
            while n > u >= 0 and n > v >= 0:
                board[u][v] += val
                u -=1
                v -=1
            
            u,v = i,j
            while n > u >= 0 and n > v >= 0:
                board[u][v] += val
                u -=1
                v +=1
            
            u,v = i,j
            while n > u >= 0 and n > v >= 0:
                board[u][v] += val
                u +=1
                v -=1
            
            board[i][j] -= val*5
            
        #count = 8

        def dequy(cur,index):
            nonlocal ans
            for i in range(cur,n):
                for j in range(n):
                    if board[i][j] <= 0:
                        continue
                    fill(i,j,-1)
                    """if count > 0 and index == n:
                        count-=1
                        print(i,j,board)"""
                    if index == n:
                        #print('??/')
                        """if count > 0:
                            count-=1
                            print(i,j,board)"""
                        #print(board)
                        ans+=1
                        #print(ans)
                    else:
                        dequy( i + 1 ,index + 1)
                    fill(i,j,1)
        
        dequy(0,1)
        """temp = 1
        for i in range(2,n+1):
            temp*=i"""

        return ans