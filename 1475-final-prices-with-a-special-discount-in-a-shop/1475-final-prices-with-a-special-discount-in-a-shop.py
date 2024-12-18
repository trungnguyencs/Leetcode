class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0]*n
        stack = []
        for i in range(n - 1, -1, -1):
            price = prices[i]
            while stack and stack[-1] > price:
                stack.pop()
            ans[i] = price - stack[-1] if stack else price
            stack.append(price)
        return ans