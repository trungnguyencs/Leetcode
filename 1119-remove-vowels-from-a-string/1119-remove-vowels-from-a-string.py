class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = 'aeiou'
        ans = []
        for ch in s:
            if ch not in vowels:
                ans.append(ch)
        return ''.join(ans)