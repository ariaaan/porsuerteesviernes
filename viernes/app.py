"""Viernes."""
from loguru import logger

from twitter import twitter_auth, generate_tweet


def lambda_handler(event=None, context=None):
    friday_tweet()


def friday_tweet():
    # Get twitter API
    twitter_api = twitter_auth()

    # Get zy tweet 
    logger.info("Generating tweet")
    tweet = generate_tweet()
    logger.info(f"Generated tweet: {tweet}")
    logger.info(f"Updating status")
    twitter_api.update_status(status=tweet)
    logger.info(f"Status was successfully updated")


if __name__ == "__main__":
    friday_tweet()
