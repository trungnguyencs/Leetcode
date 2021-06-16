class Solution:
    def wallsAndGates(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = deque([(r, c, 0) for r in range(len(matrix)) for c in range(len(matrix[0])) if matrix[r][c] == 0])
        while q:
            r, c, d = q.popleft()
            neighs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for x, y in neighs:
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == 2147483647:
                    matrix[x][y] = d + 1
                    q.append((x, y, d + 1))