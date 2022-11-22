class Solution:
    def isStrobogrammatic(self, s: str) -> bool:
        dic = {'6':'9', '9':'6', '8':'8', '0':'0', '1':'1'}
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] not in dic or dic[s[l]] != s[r]: return False
            l += 1
            r -= 1
        return True