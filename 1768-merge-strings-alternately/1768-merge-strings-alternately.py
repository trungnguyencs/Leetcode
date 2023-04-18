class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        for i in range(min(len(word1), len(word2))):
            ans.append(word1[i])
            ans.append(word2[i])
        ans.extend(word1[i+1:] if i < len(word1) - 1 else word2[i+1:])
        return ''.join(ans)