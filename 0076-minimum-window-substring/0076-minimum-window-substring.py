class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        counter = Counter(t)        # counts of required chars
        need = len(counter)         # number of unique chars we still need
        minWindow = s + '#'         # sentinel longer than any valid window
        for r, ch in enumerate(s):
            if ch not in counter:
                # expand r until we include chars we care about
                continue
            counter[ch] -= 1
            if counter[ch] == 0:
                need -= 1           # satisfied one unique char
            # Contract from the left while valid
            while need == 0:
                # update answer if smaller window found
                minWindow = min(minWindow, s[l:r+1], key=len)
                if s[l] in counter:
                    counter[s[l]] += 1
                    if counter[s[l]] == 1:
                        need += 1   # no longer valid
                l += 1
        return '' if minWindow == s + '#' else minWindow