class Solution:
    def partitionString(self, s: str) -> int:
        visited = set()
        ans = 1
        for ch in s:
            if ch not in visited:
                visited.add(ch)
            else:
                visited = {ch}
                ans += 1
        return ans