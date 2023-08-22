class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber:
            ch = chr(ord('A') + (columnNumber - 1) % 26) if columnNumber % 26 != 0 else 'Z'
            ans.append(ch)
            columnNumber = (columnNumber - 1)//26
        return ''.join(reversed(ans))