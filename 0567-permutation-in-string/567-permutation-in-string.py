class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        uniqCount = len(counter)
        w = len(s1) # sliding window size w
        for r, ch in enumerate(s2):
            if r >= w:
                leftChar = s2[r - w]
                if leftChar in counter:
                    counter[leftChar] += 1
                    if counter[leftChar] == 1:
                        uniqCount += 1
            if ch in counter:
                counter[ch] -= 1
                if counter[ch] == 0:
                    uniqCount -= 1
                    if uniqCount == 0:
                        return True
        return False