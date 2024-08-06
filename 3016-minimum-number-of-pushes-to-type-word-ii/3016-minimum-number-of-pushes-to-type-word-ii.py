class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        counter = Counter(word)
        arr = sorted(counter.values(), reverse=True)
        for i, freq in enumerate(arr):
            ans += freq * (1 + i//8)
        return ans