class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            ans.append([a + b for a, b in zip([0] + ans[-1], ans[-1] + [0])])
        return ans