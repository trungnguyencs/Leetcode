class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for _ in range(rowIndex):
            ans = [x + y for x, y in zip([0]+ans, ans+[0])]
        return ans
