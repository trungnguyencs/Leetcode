class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}
        cur = (0, 0)
        for direction in path:
            cur = self.move(cur, direction)
            if cur in visited: return True
            visited.add(cur)
        return False
    
    def move(self, cur, direction):
        x, y = cur
        if direction == 'N':
            return (x, y + 1)
        if direction == 'S':
            return (x, y - 1)
        if direction == 'W':
            return (x + 1, y)
        if direction == 'E':
            return (x - 1, y)