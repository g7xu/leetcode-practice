# class user:
#     def __init__(self):
#         self.following = set()
#         self.tweets = []

#     def add_tweet(self, tweetId):
#         self.tweets.append(tweetId)

#     def add_following(self, userId):
#         self.following.add(userId)
        
#     def unfollow(self, userId):
#         self.following.remove(userId)


from heapq import heappop, heappush
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.following = defaultdict(set) # follower -> following
        self.perUserHeap = defaultdict(list)
        self.t = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        heappush(
            self.perUserHeap[userId],
            (-self.t, tweetId)
        )
        self.t += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []
        backtrack = []
      
        for followee in self.following[userId] | {userId}:
            if self.perUserHeap[followee]:
                heappush(maxHeap, (*heappop(self.perUserHeap[followee]), followee))

        while len(res) != 10:
            if not maxHeap:
                break

            max_t, max_id, max_followee = heappop(maxHeap)
            
            res.append(max_id)
            backtrack.append((max_t, max_id, max_followee))
            
            if self.perUserHeap[max_followee]:
                
                heappush(maxHeap, (*heappop(self.perUserHeap[max_followee]), max_followee))

        # adding everything back
        for bt, bid, bf in backtrack + maxHeap:
            heappush(self.perUserHeap[bf], (bt, bid))

        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        # print(self.following[followerId], followeeId)
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)