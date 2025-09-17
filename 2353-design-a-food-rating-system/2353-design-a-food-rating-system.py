from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.ratings = {}
        self.categories = {}
        self.sortedRatings = defaultdict(SortedList)
        for food, category, rating in zip(foods, cuisines, ratings):
            self.ratings[food] = rating
            self.categories[food] = category
            self.sortedRatings[category].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        oldRating = self.ratings[food]
        category = self.categories[food]
        self.ratings[food] = newRating
        self.sortedRatings[category].remove((-oldRating, food))
        self.sortedRatings[category].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.sortedRatings[cuisine][0][1] 


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)