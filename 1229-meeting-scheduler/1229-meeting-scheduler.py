class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(); slots2.sort()
        i = j = 0
        while i < len(slots1) and j < len(slots2):
            (s1, e1), (s2, e2) = slots1[i], slots2[j]
            maxStart, minEnd = max(s1, s2), min(e1, e2)
            if maxStart + duration <= minEnd: return [maxStart, maxStart + duration]
            if e1 < e2:
                i += 1
            else:
                j += 1
        return []