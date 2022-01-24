class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        dic = {'6':'9', '9':'6', '8':'8', '0':'0', '1':'1'}
        i, j = 0, len(num)-1
        while i <= j:
            if num[i] not in dic or num[j] not in dic: return False
            if dic[num[i]] != num[j]: return False
            i += 1
            j -= 1
        return True