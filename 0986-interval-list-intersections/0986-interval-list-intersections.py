class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0
        while i < len(A) and j < len(B):
            s1, e1 = A[i]
            s2, e2 = B[j]
            maxStart, minEnd = max(s1, s2), min(e1, e2)
            if maxStart <= minEnd:
                ans.append([maxStart, minEnd])
            if e1 < e2:
                i += 1
            else:
                j += 1
        return ans