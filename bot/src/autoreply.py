import json
import logging
import os

import tweepy

from config import get_client

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class AutoReply(tweepy.StreamingClient):
    def __init__(self, *args):
        super().__init__(*args)

    def on_tweet(self, tweet):
        logger.info(f"Processing tweet:{tweet}")
        try:
            client = get_client()
            reply = (
                "Get daily email alerts for new jobs. Get notified about  new job posts on your favorite Somali "
                "job posting sites for free. Find out more and subscribe here http://www.diractly.com/ "
            )
            response = client.get_tweet(
                id=tweet.id, tweet_fields=["created_at", "author_id"]
            )
            if response.data.get("author_id") != client.get_me().data.get("id"):
                client.create_tweet(
                    text=reply,
                    user_auth=True,
                    in_reply_to_tweet_id=tweet.id,
                )
        except Exception as e:
            logger.error("Error on reply", exc_info=True)

    def on_error(self, status):
        logger.error(status)


def main(hashtag):
    client = get_client()
    tweets_listener = AutoReply(client.bearer_token)
    rule = tweepy.StreamRule(hashtag)
    tweets_listener.add_rules(add=rule)
    tweets_listener.filter()


if __name__ == "__main__":
    main(["#somalijobs"])
