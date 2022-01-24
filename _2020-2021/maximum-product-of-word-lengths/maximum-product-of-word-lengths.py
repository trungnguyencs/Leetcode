class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words = list(map(lambda w: [self.toBinary(w), len(w)], words))
        maxProd = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if words[i][0] & words[j][0] == 0:
                    maxProd = max(maxProd, words[i][1] * words[j][1])
        return maxProd
    
    def toBinary(self, word):
        return sum([1 << (ord(c) - ord('a') + 1) for c in set(word)])