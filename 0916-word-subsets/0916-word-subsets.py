class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        masterCounter = Counter()
        for word in words2:
            counter = Counter(word)
            for ch, freq in counter.items():
                masterCounter[ch] = max(masterCounter[ch], freq)
        ans = []
        for word in words1:
            counter = Counter(word)
            if all(freq <= counter[ch] for ch, freq in masterCounter.items()):
                ans.append(word)
        return ans