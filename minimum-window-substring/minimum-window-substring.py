class Solution:
    def minWindow(self, long: str, short: str) -> str:
        counter = Counter(short)
        l, count = 0, len(counter)
        ans = 0, len(long)
        for r, ch in enumerate(long):
            if ch not in counter: continue
            counter[ch] -= 1
            if counter[ch] == 0: count -= 1
            while count == 0:
                ans = min(ans, (l, r), key=lambda x: x[1] - x[0])
                if long[l] in counter:
                    counter[long[l]] += 1
                    if counter[long[l]] > 0: count += 1
                l += 1
        return "" if ans == (0, len(long)) else long[ans[0]:ans[1]+1]