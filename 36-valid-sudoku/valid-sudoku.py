class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if any( count > 1 and key != '.' for key,count in Counter(board[i]).items()):
                return False
            temp = []
            for j in range(9):
                temp.append(board[j][i])
            if any( count > 1 and key != '.' for key,count in Counter(temp).items()):
                    return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                temp = []
                for u in range(3):
                    for v in range(3):
                        temp.append(board[i+u][j+v])
                if any( count > 1 and key != '.' for key,count in Counter(temp).items()):
                    return False
        return True