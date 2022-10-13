class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len(set(self.convertWordToMorse(word) for word in words))
    
    def convertWordToMorse(self, word):
        morseTable = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        code = []
        for ch in word:
            code.append(morseTable[ord(ch) - ord('a')])
        return ''.join(code)