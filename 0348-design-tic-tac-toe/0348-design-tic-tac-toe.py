class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0]*n
        self.cols = [0]*n
        self.diag = 0
        self.codiag = 0

    def move(self, r: int, c: int, player: int) -> int:
        score = 1 if player == 1 else -1
        self.rows[r] += score
        self.cols[c] += score
        if r == c:
            self.diag += score
        if r == self.n - 1 - c:
            self.codiag += score
        if self.n in [abs(self.rows[r]), abs(self.cols[c]), abs(self.diag), abs(self.codiag)]:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)