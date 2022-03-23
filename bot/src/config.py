import logging
import os

import tweepy
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger()


def get_client():
    api_key = os.getenv("api_key")
    api_secret_key = os.getenv("api_secret_key")
    access_token = os.getenv("access_token")
    access_token_secret = os.getenv("access_token_secret")
    bearer_token = os.getenv("bearer_token")
    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=api_key,
        consumer_secret=api_secret_key,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )

    return client
