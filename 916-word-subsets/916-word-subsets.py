class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        ans = []
        counterB = Counter()
        for word in B:
            tmpCounter = Counter(word)
            for c in tmpCounter:
                counterB[c] = max(counterB[c], tmpCounter[c])
        for word in A:
            tmpCounter = Counter(word)
            if all([counterB[c] <= tmpCounter[c] for c in counterB]): ans.append(word)
        return ans