class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        #finding all good sequences will time out
        #instead, try to fill number from large to small. The first good sequence will be the answer
        self.ans = []
        if self.backtrack([0]*(2 * n - 1), 0, set(), n):
            return self.ans

    def backtrack(self, arr, i, visited, n):
        if i == len(arr):
            self.ans = arr[:]
            return True
        if arr[i] != 0:
            return self.backtrack(arr, i + 1, visited, n)
        for num in range(n, 0, -1):
            if num in visited: continue
            if num == 1:
                arr[i] = 1; visited.add(1)
                if self.backtrack(arr, i + 1, visited, n):
                    return True
                visited.remove(1); arr[i] = 0
            if i + num < len(arr) and arr[i] == arr[i + num] == 0:
                arr[i] = arr[i + num] = num; visited.add(num)
                if self.backtrack(arr, i + 1, visited, n):
                    return True
                arr[i] = arr[i + num] = 0; visited.remove(num)
        return False