class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        cur = 0
        
        visit = set()
        queue = deque([(1,0)])
        
        while queue:
            pos, moves = queue.popleft()
            for i in range(1,7):
                next_pos = pos + i
                if next_pos > n*n:
                    continue
                r,c = self.coordinate( next_pos , n )
                if board[r][c] != -1:
                    next_pos = board[r][c]
                if next_pos == n*n:
                    return moves + 1
                if next_pos not in visit:
                    visit.add(next_pos)
                    queue.append((next_pos,moves+1))
        return -1
    

    def coordinate( self, cur , n ):
        r = (cur-1)//n
        row = n - 1 - r
        col = (cur - 1)%n if not r % 2 else n - 1 - (cur - 1)%n
        return row, col
