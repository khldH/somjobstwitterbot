import os

import boto3
from dotenv import load_dotenv

from config import get_client
from dailyjobs import get_new_jobs_posted_today, tweet_jobs_posted_today

load_dotenv()

db = boto3.resource(
    "dynamodb",
    region_name=os.getenv("AWS_REGION_NAME"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

client = get_client()

if __name__ == "__main__":
    jobs = get_new_jobs_posted_today(db)
    tweet_jobs_posted_today(jobs=jobs, client=client)
