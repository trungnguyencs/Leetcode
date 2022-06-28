class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        visited = set()
        ans = 0
        for count in counter.values():
            while count in visited and count > 0:
                count -= 1
                ans += 1
            visited.add(count)
        return ans