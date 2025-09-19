class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = [[0]*26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        r, c = self._getRC(cell)
        self.grid[r][c] = value

    def resetCell(self, cell: str) -> None:
        r, c = self._getRC(cell)
        self.grid[r][c] = 0

    def getValue(self, formula: str) -> int:
        num1, num2 = formula[1:].split('+')
        if num1.isnumeric():
            num1 = int(num1)
        else:
            r, c = self._getRC(num1)
            num1 = self.grid[r][c]
        if num2.isnumeric():
            num2 = int(num2)
        else:
            r, c = self._getRC(num2)
            num2 = self.grid[r][c]
        return num1 + num2 

    def _getRC(self, s):
        r = int(s[1:]) - 1 #index starts at 1
        c = ord(s[0]) - ord('A')
        return r, c


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)