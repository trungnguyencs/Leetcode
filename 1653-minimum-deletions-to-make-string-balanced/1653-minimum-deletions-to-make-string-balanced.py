class Solution:
    def minimumDeletions(self, s: str) -> int:
        aCount = s.count('a')
        a = b = 0
        ans = len(s)
        for i, ch in enumerate(s):
            #delete all prior b and future a
            if ch == 'a':
                a += 1
                rightA = aCount - a
                ans = min(ans, b + rightA)
                
            else:
                ans = min(ans, b + aCount - a)
                b += 1
        return ans