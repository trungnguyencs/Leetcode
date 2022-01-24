class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        counter = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if secret[i] not in counter:
                    counter[secret[i]] = [0, 0]
                if guess[i] not in counter:
                    counter[guess[i]] = [0, 0]
                counter[secret[i]][0] += 1
                counter[guess[i]][1] += 1
        cows = sum([min(val) for val in counter.values()])
        return "{b}A{c}B".format(b = bulls, c = cows)