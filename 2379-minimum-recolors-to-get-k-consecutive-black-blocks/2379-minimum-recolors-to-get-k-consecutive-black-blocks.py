class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whiteCount = 0
        ans = k
        for i, color in enumerate(blocks):
            if color == 'W':
                whiteCount += 1
            if i >= k and blocks[i-k] == 'W':
                whiteCount -= 1
            if i >= k - 1:
                ans = min(ans, whiteCount)
        return ans