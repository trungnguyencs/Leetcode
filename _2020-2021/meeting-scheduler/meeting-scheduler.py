class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        i = j = 0
        while i < len(slots1) and j < len(slots2):
            s1, e1 = slots1[i]
            s2, e2 = slots2[j]
            maxS, minE = max(s1, s2), min(e1, e2)
            if maxS + duration <= minE: return [maxS, maxS + duration]
            if e1 == minE: i += 1
            else: j += 1
        return []      