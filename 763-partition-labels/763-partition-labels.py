class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        lastIndex = {ch: i for i, ch in enumerate(s)}
        l = endIndex = 0
        for r, ch in enumerate(s):
            endIndex = max(endIndex, lastIndex[ch])
            if r == endIndex:
                ans.append(r - l + 1)
                l = r + 1
        return ans