class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        self.s1, self.s2, self.s3 = s1, s2, s3
        self.dp = {}
        return self.helper(len(s1)-1, len(s2)-1, len(s3)-1)
    
    def helper(self, i1, i2, i):
        if i == -1: return True
        if i1 == -1: return self.s2[i2] == self.s3[i] and self.helper(i1, i2-1, i-1)
        if i2 == -1: return self.s1[i1] == self.s3[i] and self.helper(i1-1, i2, i-1)
        if self.s3[i] not in (self.s1[i1], self.s2[i2]): return False
        if (i1-1, i2, i-1) not in self.dp: self.dp[(i1-1, i2, i-1)] = self.helper(i1-1, i2, i-1)
        dp1 = self.dp[(i1-1, i2, i-1)]
        if (i1, i2-1, i-1) not in self.dp: self.dp[(i1, i2-1, i-1)] = self.helper(i1, i2-1, i-1)
        dp2 = self.dp[(i1, i2-1, i-1)]
        return (self.s1[i1] == self.s3[i] and dp1) or (self.s2[i2] == self.s3[i] and dp2)