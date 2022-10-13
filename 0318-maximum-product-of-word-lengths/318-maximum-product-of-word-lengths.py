class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dic = {w: self.wordToBinary(w) for w in words}
        maxProd = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if dic[words[i]] & dic[words[j]] == 0:
                    maxProd = max(maxProd, len(words[i]) * len(words[j]))
        return maxProd
    
    def wordToBinary(self, w):
        binary = 0
        for ch in set(w):
            binary |= 1 << (ord(ch) - ord('a'))
        return binary    