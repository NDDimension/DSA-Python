"""
Design Twitter

A class to simulate the core functionalities of a miniature Twitter service.

Methods:
--------
postTweet(userId: int, tweetId: int) -> None:
    Compose a new tweet by the user with userId.

getNewsFeed(userId: int) -> List[int]:
    Retrieve the 10 most recent tweet IDs in the user's news feed.
    Each item in the news feed must be posted by users who the user followed or by the user themselves.
    Tweets must be ordered from most recent to least recent.

follow(followerId: int, followeeId: int) -> None:
    Follower follows a followee. If the operation is invalid, it should be a no-op.

unfollow(followerId: int, followeeId: int) -> None:
    Follower unfollows a followee. If the operation is invalid, it should be a no-op.

Optimal Approach:
-----------------
- Store tweets in a dictionary mapping userId -> deque of (timestamp, tweetId).
- Use a global timestamp to maintain chronological order.
- Use a min-heap to merge tweets from self and followed users to efficiently get top 10 recent tweets.
- Each user has a follow set to track followees.

Time Complexity:
----------------
- postTweet: O(1)
- follow/unfollow: O(1)
- getNewsFeed: O(N log k), where N is number of followees, k is number of tweets per user (up to 10)

Example:
--------
twitter = Twitter()
twitter.postTweet(1, 5)
twitter.getNewsFeed(1)            # -> [5]
twitter.follow(1, 2)
twitter.postTweet(2, 6)
twitter.getNewsFeed(1)            # -> [6, 5]
twitter.unfollow(1, 2)
twitter.getNewsFeed(1)            # -> [5]
"""

from collections import deque, defaultdict
import heapq, time


class Twitter:
    def __init__(self) -> None:
        self.timestamp = 0  # Global timestamp to maintain chronological order
        self.tweets = defaultdict(deque)  # userId -> deque of (timestamp, tweetId)
        self.follows = defaultdict(set)  # userId -> set of followees

    def postTweet(self, userId, tweetId):
        self.timestamp += 1
        self.tweets[userId].appendleft((self.timestamp, tweetId))

        # keep only 10 most recent tweets/user

        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()

    def getNewsFeed(self, userId):
        minheap = []

        # Inc users own tweets
        users = self.follows[userId] | {userId}
        for uid in users:
            for tweet in self.tweets[uid]:
                heapq.heappush(minheap, tweet)
                if len(minheap) > 10:
                    heapq.heappop(minheap)

        # Extract tweets from heap and sort them from most recent to least
        return [tweetId for _, tweetId in sorted(minheap, reverse=True)]

    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.follows[followerId].discard(followeeId)


user = Twitter()

for i in range(1, 10):
    user.postTweet(i, i)
    print(user.getNewsFeed(i))

    user.follow(i, i + 1)
    user.postTweet(i + 1, i + 1)
    print(user.getNewsFeed(i))

    user.unfollow(i, i + 1)
    print(user.getNewsFeed(i))
