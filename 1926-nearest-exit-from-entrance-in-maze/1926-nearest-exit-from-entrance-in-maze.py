class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque([(entrance, 1)])
        visited = set([tuple(entrance)])
        while q:
            (r, c), d = q.popleft()
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if (not 0 <= nr < len(maze)) or (not 0 <= nc < len(maze[0])) or (nr, nc) in visited or maze[nr][nc] == '+': continue
                if nr in [0, len(maze) - 1] or nc in [0, len(maze[0]) - 1]: return d
                q.append(((nr, nc), d + 1))
                visited.add((nr, nc))
        return -1