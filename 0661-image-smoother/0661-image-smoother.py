class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        R, C = len(img), len(img[0])
        ans = [[0]*C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                neighs = [img[nr][nc] for nr in (r-1, r, r+1) for nc in (c-1, c, c+1) if 0 <= nr < R and 0 <= nc < C]
                ans[r][c] = sum(neighs)//len(neighs)
        return ans