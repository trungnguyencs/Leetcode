class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        minDistance = float('inf')
        q = deque([start])
        visited = {tuple(start): 0}
        while q:
            r, c = q.popleft()
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dr, dc in directions:
                nr, nc, nd = r, c, visited[(r, c)]
                while 0 <= nr + dr < len(maze) and 0 <= nc + dc < len(maze[0]) and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                    nd += 1
                if [nr, nc] == destination: minDistance = min(minDistance, nd)
                if nd > minDistance: continue
                if (nr, nc) not in visited or visited[(nr, nc)] > nd:
                    visited[(nr, nc)] = nd
                    q.append((nr, nc))
        return -1 if minDistance == float('inf') else minDistance