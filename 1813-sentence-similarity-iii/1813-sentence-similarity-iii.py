class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        dq1 = deque(s1.split())
        dq2 = deque(s2.split())
        while dq1 and dq2 and dq1[0] == dq2[0]:
            dq1.popleft()
            dq2.popleft()
        while dq1 and dq2 and dq1[-1] == dq2[-1]:
            dq1.pop()
            dq2.pop()
        return not dq1 or not dq2