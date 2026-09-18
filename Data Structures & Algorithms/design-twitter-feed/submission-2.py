class Twitter:

    def __init__(self):
        self.posts = []
        heapq.heapify(self.posts)
        self.follows = {}
        self.postID = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.posts, (-1 * self.postID, [userId, tweetId]))
        self.postID += 1

        if userId not in self.follows:
            self.follows[userId] = set()
            self.follows[userId].add(userId)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        count = 0 
        posts = self.posts.copy()
        heapq.heapify(posts)
        while posts: 
            post = heapq.heappop(posts)
            if post[1][0] in self.follows[userId]:
                feed.append(post[1][1])
                count += 1

            if count == 10:
                break
                
        return feed

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.follows:
            self.follows[followerId] = set()

        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if not followeeId in self.follows:
            return

        self.follows[followerId].discard(followeeId)
        
