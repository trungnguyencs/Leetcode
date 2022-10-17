class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == ord('z') - ord('a') + 1