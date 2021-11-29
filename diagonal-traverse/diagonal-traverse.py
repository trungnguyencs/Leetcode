class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                dic[r + c].append(mat[r][c])
        ans = []
        for i in range(len(mat) + len(mat[0]) - 1):
            ans.extend(dic[i] if i % 2 == 1 else reversed(dic[i]))
        return ans