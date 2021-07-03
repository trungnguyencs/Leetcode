class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        tableA = defaultdict(lambda: defaultdict(int))
        tableB = defaultdict(lambda: defaultdict(int))
        C = [[0]*len(B[0]) for _ in range(len(A))] 
        for r in range(len(A)):
            for c in range(len(A[0])):
                if A[r][c] != 0: tableA[r][c] = A[r][c]
        for r in range(len(B)):
            for c in range(len(B[0])):
                if B[r][c] != 0: tableB[r][c] = B[r][c]
        for rA in tableA:
            for cA in tableA[rA]:
                if cA not in tableB: continue
                for cB in tableB[cA]: # cA == rB
                    C[rA][cB] += tableA[rA][cA] * tableB[cA][cB]
        return C