class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        if not spaces: return s
        ans = []
        j = 0
        for i, ch in enumerate(s):
            if j < len(spaces) and i == spaces[j]:
                ans.append(' ')
                j += 1
            ans.append(ch)
        return ''.join(ans)