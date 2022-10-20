class Solution:
    def intToRoman(self, num: int) -> str:
        arr = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
               (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), 
               (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        ans = []
        for amount, letter in arr:
            if num >= amount:
                occurence = num // amount
                num -= amount * occurence
                ans.append(letter * occurence)
            if num == 0: break
        return ''.join(ans)