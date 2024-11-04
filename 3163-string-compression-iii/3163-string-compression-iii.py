class Solution:
    def compressedString(self, word: str) -> str:
        curCh, curCount = word[0], 1
        ans = []
        for i in range(1, len(word)):
            if word[i] != curCh or curCount == 9:
                ans.extend([str(curCount), curCh])
                curCh, curCount = word[i], 1
            else:
                curCount += 1
        ans.extend([str(curCount), curCh])
        return ''.join(ans)