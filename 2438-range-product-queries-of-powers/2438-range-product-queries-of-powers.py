class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        #convert number to binary string to find the powers of two array
        MOD = 10**9 + 7
        binary = bin(n)[2:]
        arr = []
        for i, ch in enumerate(reversed(binary)):
            if ch == '1':
                arr.append(2**i)
        prefixProd = [1]
        for num in arr:
            prefixProd.append(num * prefixProd[-1])
        return [prefixProd[r+1]//prefixProd[l] % MOD for l, r in queries]