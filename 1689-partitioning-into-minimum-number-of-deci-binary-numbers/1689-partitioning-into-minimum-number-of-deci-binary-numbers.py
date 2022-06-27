class Solution:
    def minPartitions(self, s: str) -> int:
        return max(int(ch) for ch in s)