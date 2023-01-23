class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        votes = [0]*(n + 1)
        for a, b in trust:
            votes[a] -= 1
            votes[b] += 1
        for i in range(1, len(votes)):
            if votes[i] == n - 1: return i
        return -1