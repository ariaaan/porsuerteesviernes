"""Twitter."""
import emojis
import tweepy

import settings


VIDEO_URL = "https://www.youtube.com/watch?v=WZC5VsqKqH8&t=77s"


def generate_tweet():
    return f"Pero por suerte es viernes {emojis.get_random_friday_emoji()}! @zambayonny\n\n{VIDEO_URL}"


def twitter_auth():
    auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_SECRET_KEY)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    
    return api
