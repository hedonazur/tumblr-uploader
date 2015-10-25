import json
with open("config.json", "r") as handle:
	secrets = json.loads(handle.read())
	
consumer_key = secrets["consumer_key"]
consumer_secret = secrets["consumer_secret"]
token_key = secrets["token_key"]
token_secret = secrets["token_secret"]
youtube_key = secrets["youtube_key"]