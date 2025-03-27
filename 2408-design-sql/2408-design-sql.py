class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.db = {name: Table(columnCount) for name, columnCount in zip(names, columns)}

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.db:
            return False
        return self.db[name].insertRow(row)

    def rmv(self, name: str, rowId: int) -> None:
        if name in self.db:
            self.db[name].removeRow(rowId)

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.db:
            return "<null>"
        return self.db[name].selectCell(rowId, columnId)

    def exp(self, name: str) -> List[str]:
        if name not in self.db: return []
        return self.db[name].export()

class Table:

    def __init__(self, columnCount):
        self.columnCount = columnCount
        self.rowCount = 0
        self.rows = {}

    def insertRow(self, row):
        if len(row) != self.columnCount: return False
        self.rowCount += 1
        self.rows[self.rowCount] = row
        return True

    def removeRow(self, rowId):
        if rowId in self.rows:
            del self.rows[rowId]

    def selectCell(self, rowId, columnId):
        if rowId not in self.rows or columnId > self.columnCount: return "<null>"
        return self.rows[rowId][columnId - 1]

    def export(self):
        ans = []
        for rowId, row in self.rows.items():
            ans.append(','.join([str(rowId)] + row))
        return ans


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)