class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for ch in s[::-1]:
            if ch in 'IXC':
                num = num + dic[ch] if num < 5*dic[ch] else num - dic[ch]
            else:
                num += dic[ch]
        return num
​
