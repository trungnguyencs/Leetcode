class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        counter = Counter(t)
        need = len(counter)
        minWindow = s + '#'
        for r, ch in enumerate(s):
            if ch not in counter: continue
            counter[ch] -= 1
            if counter[ch] == 0: need -= 1
            while need == 0:
                minWindow = min(minWindow, s[l:r + 1], key=len)
                if s[l] in counter:
                    counter[s[l]] += 1
                    if counter[s[l]] == 1: need += 1
                l += 1
        return '' if minWindow == s + '#' else minWindow