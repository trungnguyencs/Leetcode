class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for op in operations:
            ans += 1 if '+' in op else -1
        return ans
