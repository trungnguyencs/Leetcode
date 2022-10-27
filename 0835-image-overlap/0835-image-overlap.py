class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        img1Pts, img2Pts = [], []
        dic = defaultdict(int)
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1: img1Pts.append((r, c))
                if img2[r][c] == 1: img2Pts.append((r, c))
        for r1, c1 in img1Pts:
            for r2, c2 in img2Pts:
                dr, dc = r2 - r1, c2 - c1
                dic[dr, dc] += 1
        return max(dic.values()) if dic else 0