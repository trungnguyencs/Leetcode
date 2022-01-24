class Solution:
    def frequencySort(self, s: str) -> str:
        sortedCounter = sorted([(freq, ch) for ch, freq in Counter(s).items()], reverse=True)
        return ''.join([ch*freq for freq, ch in sortedCounter])