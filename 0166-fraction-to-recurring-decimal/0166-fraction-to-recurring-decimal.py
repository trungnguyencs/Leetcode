class Solution:
    def fractionToDecimal(self, a: int, b: int) -> str:
        sign = '-' if a * b < 0 else ''
        ans = [sign]
        n, remain = divmod(abs(a), abs(b))
        if remain == 0:
            ans.append(str(n))
            return ''.join(ans)
        ans.append(str(n) + '.')
        dic = {}
        while remain != 0:
            #index in the result string where the digit from this remainder will be placed
            #so we know exactly where to insert '('
            dic[remain] = len(ans)
            print(dic[remain])
            n, remain = divmod(remain * 10, abs(b))
            ans.append(str(n))
            if remain in dic:
                ans.insert(dic[remain], '(')
                ans.append(')')
                return ''.join(ans)
        return ''.join(ans)