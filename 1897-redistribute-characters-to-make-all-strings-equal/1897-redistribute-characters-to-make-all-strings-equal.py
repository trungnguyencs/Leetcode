class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = Counter()
        for word in words:
            for ch in word:
                counter[ch] += 1
        return all(counter[ch] % len(words) == 0 for ch in counter)