class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = cur = 0
        for d in gain:
            cur += d
            highest = max(highest, cur)
        return highest