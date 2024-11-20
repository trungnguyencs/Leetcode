class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counter = Counter(s)
        if min(counter['a'], counter['b'], counter['c']) < k: return -1
        for ch in counter:
            counter[ch] -= k
        n, l = len(s), 0
        ans = float('inf')
        ct = Counter()
        for r, ch in enumerate(s):
            ct[ch] += 1
            while ct[ch] > counter[ch]:
                ct[s[l]] -= 1
                l += 1
            ans = min(ans, n - (r - l + 1))
        return ans