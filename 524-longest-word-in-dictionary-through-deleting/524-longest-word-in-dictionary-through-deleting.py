class Solution:
    # def findLongestWord(self, s: str, dictionary: List[str]) -> str:
    #     ans = ''
    #     for string in dictionary:
    #         if self.isSubsequence(string, s):
    #             ans = min(ans, string, key=lambda x: (-len(x), x))
    #     return ans
        
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x)) # front has max len, min lexicographical order
        for word in d:
            if self.isSubsequence(word, s): return word
        return ''
    
    def isSubsequence(self, short, long):
        i = 0
        for ch in long:
            if ch == short[i]:
                i += 1
            if i == len(short): return True
        return False