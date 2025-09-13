class Solution:
    def maxFreqSum(self, s: str) -> int:
        vCounter = Counter()
        cCounter = Counter()
        maxVCounter = 0
        maxCCounter = 0
        for ch in s:
            if ch in 'aeiou':
                vCounter[ch] += 1
                maxVCounter = max(maxVCounter, vCounter[ch])
            else:
                cCounter[ch] += 1
                maxCCounter = max(maxCCounter, cCounter[ch])
        return maxVCounter + maxCCounter