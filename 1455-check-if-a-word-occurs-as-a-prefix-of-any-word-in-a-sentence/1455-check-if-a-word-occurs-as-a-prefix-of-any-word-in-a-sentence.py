class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        n = len(searchWord)
        for i, word in enumerate(sentence.split()):
            if len(word) >= n and word[:n] == searchWord:
                return i + 1
        return -1