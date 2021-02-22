class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newS, newE = newInterval
        left, right = [], []
        for s, e in intervals:
            if e < newS: left.append([s, e])
            elif s > newE: right.append([s, e])
            else: newS, newE = min(newS, s), max(newE, e)
        return left + [[newS, newE]] + right