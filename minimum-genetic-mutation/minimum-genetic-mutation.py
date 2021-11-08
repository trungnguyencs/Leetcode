class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        q = deque([start])
        visited = set([start])
        step = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == end: return step
                for neigh in self.findNextNeighbors(cur):
                    if neigh in visited or neigh not in bank:
                        continue
                    visited.add(neigh)
                    q.append(neigh)
            step += 1
        return -1
        
    def findNextNeighbors(self, s):
        ans = []
        for i, ch in enumerate(s):
            for newCh in 'ACGT':
                if newCh == ch: continue
                ans.append(s[:i] + newCh + s[i+1:])
        return ans