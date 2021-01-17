class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            chL, chR = s[i].lower(), s[j].lower()
            if not chL.isalnum():
                i += 1
            elif not chR.isalnum():
                j -= 1
            elif chL != chR:
                return False
            else:
                i += 1
                j -= 1
        return True
