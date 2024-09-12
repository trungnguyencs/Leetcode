class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        allowed = set(allowed)
        for word in words:
            if all(ch in allowed for ch in word):
                ans += 1
        return ans