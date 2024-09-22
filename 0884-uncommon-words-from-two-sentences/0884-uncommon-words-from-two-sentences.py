class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = Counter(s1.split())
        words2 = Counter(s2.split())
        ans = []
        for w, freq in words1.items():
            if w not in words2 and freq == 1:
                ans.append(w)
        for w, freq in words2.items():
            if w not in words1 and freq == 1:
                ans.append(w)
        return ans