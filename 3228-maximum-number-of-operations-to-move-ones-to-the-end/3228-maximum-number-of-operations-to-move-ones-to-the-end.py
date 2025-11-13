class Solution:
    def maxOperations(self, s: str) -> int:
        #optimal way is move from left to right
        #each time we see a '01', we move all the previous '1' seen so far to that point
        s = s + '1'
        ans = oneCount = 0
        for i in range(len(s) - 1):
            if s[i] == '1':
                oneCount += 1
            elif s[i+1] == '1':
                ans += oneCount
        return ans