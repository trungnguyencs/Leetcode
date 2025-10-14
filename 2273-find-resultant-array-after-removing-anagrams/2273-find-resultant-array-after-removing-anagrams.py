class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        prev = self.getCounter(words[0])
        ans = [words[0]]
        for i in range(1, len(words)):
            cur = self.getCounter(words[i])
            if cur == prev:
                continue
            ans.append(words[i])
            prev = cur
        return ans

    def getCounter(self, word):
        counter = [0] * 26
        for c in word:
            counter[ord(c) - ord('a')] += 1
        return tuple(counter)