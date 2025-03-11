class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = ans = 0
        counter = Counter()
        for r, ch in enumerate(s):
            counter[ch] += 1
            while len(counter) == 3:
                ans += len(s) - r #all the string with ending >= r will qualify
                prev = s[l]
                counter[prev] -= 1
                if counter[prev] == 0:
                    del counter[prev]
                l += 1
        return ans