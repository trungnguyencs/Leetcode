class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.G = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        self.G[userId].add(userId) #user should follow themself
        ans, heap = [], []
        for followerId in self.G[userId]:
            if not self.tweets[followerId]: continue
            timestamp, tweetId = self.tweets[followerId][-1]
            heappush(heap, (timestamp, tweetId, followerId, len(self.tweets[followerId]) - 1))
        while heap and len(ans) < 10:
            _, tweetId, followerId, i = heappop(heap)
            ans.append(tweetId)
            if i == 0: continue
            timestamp, tweetId = self.tweets[followerId][i-1]
            heappush(heap, (timestamp, tweetId, followerId, i-1))
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.G[followerId].add(followeeId) 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.G[followerId].discard(followeeId)       


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)