class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        R = len(strs)
        C = len(strs[0])
        for c in range(C):
            for r in range(1, R):
                if strs[r][c] < strs[r-1][c]:
                    ans += 1
                    break
        return ans