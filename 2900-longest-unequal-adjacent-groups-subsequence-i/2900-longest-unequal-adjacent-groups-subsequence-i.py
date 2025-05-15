class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = [words[0]]
        cur = groups[0]
        for i in range(1, len(words)):
            if groups[i] == cur: continue
            ans.append(words[i])
            cur = groups[i]
        return ans