class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        R, C = len(mat), len(mat[0])
        dic = defaultdict(list)
        for r in range(R):
            for c in range(C):
                dic[r+c].append(mat[r][c])
        ans = []
        for i, k in enumerate(sorted(dic.keys())):
            arr = dic[k]
            ans.extend(arr if i % 2 == 1 else reversed(arr))
        return ans