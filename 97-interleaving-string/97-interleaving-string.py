class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        self.s1, self.s2, self.s3 = s1, s2, s3
        return self.dp(0, 0)
    
    @cache
    def dp(self, i, j):
        if i == len(self.s1) and j == len(self.s2): return True
        if i > len(self.s1) and j > len(self.s2): return False
        ret1 = ret2 = False
        if i < len(self.s1) and self.s1[i] == self.s3[i+j]:
            ret1 = self.dp(i + 1, j)
        if j < len(self.s2) and self.s2[j] == self.s3[i+j]:
            ret2 = self.dp(i, j + 1)
        return ret1 or ret2  