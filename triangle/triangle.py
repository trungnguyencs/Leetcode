class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cur = triangle[0]
        for r in range(1, len(triangle)):
            row = triangle[r]
            nxt = [cur[0] + row[0]] + [0]*(r-1) + [cur[-1] + row[-1]]
            for i in range(1, r):
                nxt[i] = row[i] + min(cur[i], cur[i-1])
            cur = nxt
        return min(cur)