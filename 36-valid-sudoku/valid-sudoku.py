class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            m = defaultdict(int)
            for j in range(9):
                if board[i][j] != '.':
                    if m[board[i][j]]:
                        return False
                    else:
                        m[board[i][j]] = 1
        for i in range(9):
            m = defaultdict(int)
            for j in range(9):
                if board[j][i] != '.':
                    if m[board[j][i]]:
                        return False
                    else:
                        m[board[j][i]] = 1
        for i in range(0, 9 , 3):
            for j in range(0, 9, 3):
                m = defaultdict(int)
                for o in range(i, i + 3):
                    for k in range(j , j + 3):
                        if board[k][o] != '.':
                            if m[board[k][o]]:
                                return False
                            else:
                                m[board[k][o]] = 1
        return True