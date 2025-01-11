class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False
        counter = Counter(s)
        return len([freq for freq in counter.values() if freq % 2 == 1]) <= k