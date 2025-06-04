class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1: return word
        w = len(word) - numFriends + 1
        ans = ''
        for s in range(len(word)):
            e = min(s + w - 1, len(word) - 1)
            ans = max(ans, word[s: e + 1])
        return ans