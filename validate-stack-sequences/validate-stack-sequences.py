class Solution:
    # O(n) space: stack simulation
    # def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    #     stack = []
    #     i = 0
    #     for num in pushed:
    #         stack.append(num)
    #         while stack and stack[-1] == popped[i]:
    #             stack.pop()
    #             i += 1
    #     return not stack
    
    # O(1) space: use pushed as the stack
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j = -1, 0
        for num in pushed:
            i += 1
            pushed[i] = num
            while i >= 0 and pushed[i] == popped[j]:
                i -= 1
                j += 1
        return i == -1