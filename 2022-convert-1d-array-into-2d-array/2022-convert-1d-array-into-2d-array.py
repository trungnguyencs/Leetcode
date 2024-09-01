class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original): return []
        ans = [[0]*n for _ in range(m)]
        r = c = 0
        for num in original:
            ans[r][c] = num
            c += 1
            if c == n:
                r, c = r + 1, 0
        return ans