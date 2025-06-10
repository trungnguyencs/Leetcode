class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        maxOddFreq = max([freq for freq in counter.values() if freq % 2 == 1])
        minEvenFreq = min([freq for freq in counter.values() if freq % 2 == 0])
        return maxOddFreq - minEvenFreq