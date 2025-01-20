class Solution:
    def canMeasureWater(self, A: int, B: int, target: int) -> bool:
        visited = {(0, 0)}
        q = deque([(0, 0)])
        while q:
            a, b = q.popleft()
            if target in (a, b, a + b):
                return True
            nextStages = [(0, b), (A, b), (a, 0), (a, B), (min(A, a + b), max(0, a + b - A)), (max(0, a + b - B), min(B, a + b))] 
            for na, nb in nextStages:
                if (na, nb) not in visited:
                    q.append((na, nb))
                    visited.add((na, nb))
        return False