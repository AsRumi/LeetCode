"""
355. Design Twitter
"""

from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.tweets = {}
        self.connections = {}
        self.time = 0
        pass

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.setdefault(userId, []).append((tweetId, self.time))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed_heap = []
        
        # Add user's first tweet:
        user_tweets = self.tweets.get(userId, None)
        if user_tweets:
            tweetId, time = user_tweets[-1]
            feed_heap.append([time, tweetId, userId, len(user_tweets) - 1])
    
        # Add all followers' first tweet:
        user_followers = self.connections.get(userId, None)
        if user_followers:
            for follower in user_followers:
                follower_tweets = self.tweets.get(follower, None)
                if follower_tweets:
                    tweetId, time = follower_tweets[-1]
                    feed_heap.append([time, tweetId, follower, len(follower_tweets) - 1])
        
        heapq.heapify(feed_heap)
        
        tweets_count = 0
        list_of_tweets = []
        while len(feed_heap) > 0 and tweets_count < 10:
            time, tweet, user, index = heapq.heappop(feed_heap)
            list_of_tweets.append(tweet)
            user_tweets = self.tweets.get(user, None)
            if user_tweets and index > 0:
                tweetId, time = user_tweets[index - 1]
                heapq.heappush(feed_heap, [time, tweetId, user, index - 1])
            tweets_count += 1
        return list_of_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return None
        self.connections.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        target_list = self.connections.get(followerId, [])
        if followeeId in target_list:
            target_list.remove(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1, 5)
param_2 = obj.getNewsFeed(1)
print(param_2)
obj.follow(1, 2)
obj.postTweet(2, 6)
param_2 = obj.getNewsFeed(1)
print(param_2)
obj.unfollow(1, 2)
param_2 = obj.getNewsFeed(1)
print(param_2)