class Solution:
    def maximumLength(self, s: str) -> int:
        counter = Counter()
        cur = ''
        streak = 0
        for ch in s:
            if ch == cur:
                streak += 1
            else:
                cur = ch
                streak = 1
            for i in range(streak):
                counter[ch*(i + 1)] += 1
        arr = sorted(counter.keys(), key=len, reverse=True)
        for st in arr:
            if counter[st] > 2: return len(st)
        return -1