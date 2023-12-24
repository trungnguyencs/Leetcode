class Solution:
    def minOperations(self, s: str) -> int:
        same = diff = 0
        for i, ch in enumerate(s):
            if i % 2 == int(ch):
                diff += 1
            else:
                same += 1
        return min(same, diff)