class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        R, C = len(room), len(room[0])
        cleaned = set()
        visited = set()
        delta = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
        r, c, d = 0, 0, 'R'
        while (r, c, d) not in visited:
            visited.add((r, c, d))
            cleaned.add((r, c))
            dr, dc = delta[d]
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and room[nr][nc] == 0:
                r, c = nr, nc
            else:
                if d == 'U': d = 'R'
                elif d == 'D': d = 'L'
                elif d == 'R': d = 'D'
                else: d = 'U'
        return len(cleaned)