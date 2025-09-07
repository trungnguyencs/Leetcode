class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for num in range(1, n//2 + 1):
            ans.append(num)
            ans.append(-num)
        if n % 2 == 1:
            ans.append(0)
        return ans