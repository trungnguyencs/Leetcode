class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i, word in enumerate(words):
            for j, ch in enumerate(word):
                if j > len(words)-1 or i > len(words[j])-1 or ch != words[j][i]:
                    return False
        return True