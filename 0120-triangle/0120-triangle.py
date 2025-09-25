class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cur = triangle[0]
        for row in triangle[1:]:
            nxt = [cur[0] + row[0]] + [0] * (len(cur) - 1) + [cur[-1] + row[-1]]
            for i in range(1, len(cur)):
                nxt[i] = row[i] + min(cur[i-1], cur[i])
            cur = nxt
        return min(cur)