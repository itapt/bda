import os
import json
import tweepy

FILE_DIR = os.path.dirname(__file__)
CONFIG_PATH = os.path.abspath(os.path.join(FILE_DIR, "../config/config.json")) # call abspath to resolve '..'

def read_bearer_token(config_path : str) -> str:
    with open(config_path, 'r') as fd:
        config_json = json.load(fd)
        return config_json["token_bearer"]


TOKEN = read_bearer_token(CONFIG_PATH)

x_client = tweepy.Client(bearer_token=TOKEN)

x_target_user = x_client.get_user(username="tenslw")
x_target_user_id = x_target_user.data.id

tweets = x_client.get_users_tweets(id=x_target_user_id, max_results = 5)
print(tweets.data[0].text)
