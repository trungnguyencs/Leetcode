class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.w, self.h = width, height
        self.d = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        self.food = deque(food)                
        self.snake = deque([(0, 0)])
        self.pos = set([(0, 0)])

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        dr, dc = self.d[direction]
        nr, nc = self.snake[0][0] + dr, self.snake[0][1] + dc
        if not 0 <= nr < self.h or not 0 <= nc < self.w: return -1
        if self.food and [nr, nc] == self.food[0]:
            self.food.popleft()
        else:
            self.pos.remove(self.snake.pop())
        if (nr, nc) in self.pos: return -1
        self.snake.appendleft((nr, nc))
        self.pos.add((nr, nc))
        return len(self.snake) - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)