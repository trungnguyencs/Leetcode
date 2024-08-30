class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dic = {}
        for ch in "qwertyuiop":
            dic[ch] = 1
        for ch in "asdfghjkl":
            dic[ch] = 2
        for ch in "zxcvbnm":
            dic[ch] = 3
        ans = []
        for word in words:
            if all(dic[word[i].lower()] == dic[word[i+1].lower()] for i in range(len(word) - 1)):
                ans.append(word)
        return ans   