class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        ans = []
        for freq, ch in sorted([(freq, ch) for ch, freq in counter.items()], reverse=True):
            ans.extend(ch * freq)
        return ''.join(ans)