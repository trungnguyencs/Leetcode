class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        q = deque([start])
        visited = set([tuple(start)])
        while q:
            r, c = q.popleft()
            if [r, c] == destination: return True
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r, c
                while 0 <= nr + dr < len(maze) and 0 <= nc + dc < len(maze[0]) and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))
        return False