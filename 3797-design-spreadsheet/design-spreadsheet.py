class Spreadsheet:

    def __init__(self, rows: int):
        self.record = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.record[cell] = value

    def resetCell(self, cell: str) -> None:
        self.record[cell] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        fin,sen = formula.split('+')
        if 'A' <= fin[0] <= 'Z':
            fin = self.record[fin] if self.record[fin] else 0
        if 'A' <= sen[0] <= 'Z':
            sen = self.record[sen] if self.record[sen] else 0
        return int(fin) + int(sen)



# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)