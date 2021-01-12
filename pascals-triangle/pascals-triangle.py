class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        ans = [[1]]
        for _ in range(1, numRows):
            ans.append([a+b for a,b in zip([0]+ans[-1], ans[-1]+[0])])
        return ans
