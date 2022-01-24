class Solution:
    def intervalIntersection(self, list1: List[List[int]], list2: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            s1, e1 = list1[i]
            s2, e2 = list2[j]
            if s1 <= s2 <= e1 or s2 <= s1 <= e2:
                ans.append([max(s1, s2), min(e1, e2)])
            if e1 < e2:
                i += 1
            else:
                j += 1
        return ans