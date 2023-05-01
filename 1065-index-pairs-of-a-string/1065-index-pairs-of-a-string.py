class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        ans = []
        for word in words:
            ans.extend(self.helper(word, text))
        ans.sort()
        return ans
    
    def helper(self, word, text):
        w = len(word)
        return [(i, i + w - 1) for i in range(len(text) - w + 1) if text[i:i+w] == word]