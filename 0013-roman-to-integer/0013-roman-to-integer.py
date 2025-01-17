class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        #Go from back to front
        #If current char is smaller than next char, substract it. Else, add it
        ans = dic[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            curVal, nextVal = dic[s[i]], dic[s[i+1]]
            if curVal < nextVal:
                ans -= curVal
            else:
                ans += curVal
        return ans