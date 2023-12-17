from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.dic = {}
        self.data = defaultdict(SortedList)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.dic[food] = (cuisine, rating)
            self.data[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, oldRating = self.dic[food]
        self.dic[food] = cuisine, newRating
        self.data[cuisine].remove((-oldRating, food))
        self.data[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.data[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)