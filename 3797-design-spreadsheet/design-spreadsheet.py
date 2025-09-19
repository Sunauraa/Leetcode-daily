class Spreadsheet:

    def __init__(self, rows: int):
        self.record = defaultdict(dict)
        for i in range(26):
            char = chr( ord('A') + i )
            for j in range(1,rows+1):
                self.record[char][j] = 0

    def setCell(self, cell: str, value: int) -> None:
        fi,se = cell[0], int(cell[1:])
        self.record[fi][se] = value

    def resetCell(self, cell: str) -> None:
        fi,se = cell[0], int(cell[1:])
        self.record[fi][se] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        fin,sen = formula.split('+')
        #print(fin,sen)
        #print(ord(fin[0]),ord('A'),ord('Z'))
        if 'A' <= fin[0] <= 'Z':
            fi1,fi2 = fin[0], int(fin[1:])
            #print(fi1,fi2)
            fin = self.record[fi1][fi2]
        if 'A' <= sen[0] <= 'Z':
            fi1,fi2 = sen[0], int(sen[1:])
            sen = self.record[fi1][fi2]
        return int(fin) + int(sen)



# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)