class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        counter = Counter(words[0])
        for word in words[1:]:
            tmpCounter = Counter(word)
            for ch in counter:
                counter[ch] = min(counter[ch], tmpCounter[ch])
        for ch, freq in counter.items():
            for _ in range(freq):
                ans.append(ch)
        return ans