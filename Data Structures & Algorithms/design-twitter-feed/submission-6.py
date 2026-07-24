import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.users = {}
        self.tweets = {}
        self.time = 0

    def _init(self, userId: int) -> None:
        if userId not in self.users:
            self.users[userId] = {userId}

        if userId not in self.tweets:
            self.tweets[userId] = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._init(userId)

        # Store timestamp and tweet ID
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self._init(userId)

        heap = []

        # Add each followed user's most recent tweet
        for followeeId in self.users[userId]:
            self._init(followeeId)

            tweets = self.tweets[followeeId]

            if not tweets:
                continue

            index = len(tweets) - 1
            timestamp, tweetId = tweets[index]

            heapq.heappush(
                heap,
                (-timestamp, tweetId, followeeId, index)
            )

        result = []

        while heap and len(result) < 10:
            neg_time, tweetId, user, index = heapq.heappop(heap)

            result.append(tweetId)

            # Add this user's previous tweet
            previous_index = index - 1

            if previous_index >= 0:
                timestamp, previous_tweet = self.tweets[user][previous_index]

                heapq.heappush(
                    heap,
                    (-timestamp, previous_tweet, user, previous_index)
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self._init(followerId)
        self._init(followeeId)

        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self._init(followerId)

        if followerId == followeeId:
            return

        self.users[followerId].discard(followeeId)