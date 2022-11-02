class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        q = deque([(start, 0)])
        while q:
            cur, d = q.popleft()
            if cur == end: return d
            for neigh in self.getNeighbors(cur, bank):
                q.append((neigh, d + 1))
        return -1
    
    def getNeighbors(self, cur, bank):
        neighbors = []
        for i, ch in enumerate(cur):
            for newCh in 'ACGT':
                newWord = cur[:i] + newCh + cur[i+1:]
                if newWord != cur and newWord in bank:
                    neighbors.append(newWord)
                    bank.remove(newWord)
        return neighbors
                    