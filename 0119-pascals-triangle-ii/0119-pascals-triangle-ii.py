class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for _ in range(rowIndex):
            ans = [a + b for a, b in zip(ans + [0], [0] + ans)]
        return ans