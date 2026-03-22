class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target: return True
            self.rotate(mat)
        return False
        
    def rotate(self, mat):
        #rotate = reverse + flip along diagonal
        mat.reverse()
        for r in range(len(mat)):
            for c in range(r):
                mat[r][c], mat[c][r] = mat[c][r], mat[r][c]