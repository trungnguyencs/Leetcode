class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = float('inf')
        leftB = [0]*len(s)
        for i in range(len(s) - 1):
            leftB[i+1] = leftB[i] + 1 if s[i] == 'b' else leftB[i]
        rightA = 0
        for i in range(len(s) - 1, -1, -1):
            ans = min(ans, leftB[i] + rightA)
            if s[i] == 'a':
                rightA += 1
        return ans