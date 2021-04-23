class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        l = 0
        for r in range(len(s) + 1):
            if r == len(s) or s[r] == ' ':
                self.reverse(s, l, r-1)
                l = r + 1
        
    def reverse(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1