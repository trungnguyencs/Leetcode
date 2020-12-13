class TicTacToe:
​
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.rowSum = [0]*n
        self.colSum = [0]*n
        self.diagSum = self.codiagSum = 0
​
    def move(self, r: int, c: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.rowSum[r] = self.rowSum[r] + 1 if player == 1 else self.rowSum[r] - 1
        self.colSum[c] = self.colSum[c] + 1 if player == 1 else self.colSum[c] - 1
        if r == c:
            self.diagSum = self.diagSum + 1 if player == 1 else self.diagSum - 1
        if r + c == self.n - 1:
            self.codiagSum = self.codiagSum + 1 if player == 1 else self.codiagSum - 1
        if self.n in [abs(self.rowSum[r]), abs(self.colSum[c]), abs(self.diagSum), abs(self.codiagSum)]:
            return player
        return 0
    
​
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
