class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        return SparseMatrix.fromDense(A).multiply(SparseMatrix.fromDense(B)).toDense()
        
class SparseMatrix:
    def __init__(self, rowCount, colCount, dic):
        self.rowCount = rowCount
        self.colCount = colCount
        self.dic = dic
    
    @classmethod
    def fromSparse(cls, rowCount, colCount, dic):
        return cls(rowCount, colCount, dic)

    @classmethod
    def fromDense(cls, mat):
        dic = defaultdict(int)
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                dic[(r, c)] = mat[r][c]
        return cls(len(mat), len(mat[0]), dic)
    
    def toDense(self):
        mat = [[0]*self.colCount for _ in range(self.rowCount)]
        for (r, c), val in self.dic.items():
            mat[r][c] = val
        return mat
    
    def multiply(self, B):
        assert self.colCount == B.rowCount
        rowCount, colCount = self.rowCount, B.colCount
        dic = defaultdict(int)
        for (rA, cA), val in self.dic.items():
            for cB in range(B.colCount): #cA == rB
                if (cA, cB) in B.dic:
                    dic[(rA, cB)] += val*B.dic[(cA, cB)]
        return self.fromSparse(rowCount, colCount, dic)