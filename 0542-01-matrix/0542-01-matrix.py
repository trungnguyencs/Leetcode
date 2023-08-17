class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        R, C = len(mat), len(mat[0])
        ans = [[0]*C for _ in range(R)]
        q = deque([(r, c) for r in range(R) for c in range(C) if mat[r][c] == 0])
        visited = set(q)
        d = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:
                        ans[nr][nc] = d
                        visited.add((nr, nc))
                        q.append((nr, nc))
            d += 1
        return ans