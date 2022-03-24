import random
from typing import Any, List

import pandas as pd

# from src.config import get_client
from config import get_client


def post_random_tweet(tweets: List, client: Any):
    tweet = random.choice(tweets)
    tweet = tweet + "\n" + "#Somalijobs, #Somaliland, #Somalia"
    try:
        client.create_tweet(text=tweet)
        print(tweet, ": sent successfully")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    client = get_client()
    tweets_df = pd.read_csv("files/tweets.csv")
    tweets = tweets_df["tweets"].values.tolist()
    post_random_tweet(tweets, client)
