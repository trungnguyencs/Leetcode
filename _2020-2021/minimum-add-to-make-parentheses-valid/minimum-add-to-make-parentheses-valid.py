class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        ans, count = 0, 0
        for ch in S:
            if ch == '(':
                count += 1
            else:
                count -= 1
                if count < 0:
                    ans += 1
                    count = 0
        return ans + count
