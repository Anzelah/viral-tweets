import tweepy
import config

#v2 authentication for creating tweets
client = tweepy.Client(
    consumer_key=config.consumer_key,
    consumer_secret=config.consumer_secret,
    access_token=config.access_token,
    access_token_secret=config.access_token_secret,
    wait_on_rate_limit=True
)

#v1 authentication for uploading media
auth = tweepy.OAuth1UserHandler(config.consumer_key, config.consumer_secret, config.access_token, config.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#post an image with attached text
print(api.verify_credentials().screen_name)
try:
	media = api.media_upload(filename='images/mot.jpg')
	print(media)
	media_id = media.media_id_string
	client.create_tweet(text='Morning motivation', media_ids=[media_id])
except tweepy.TweepyException as e:
	print('An error occured: {}' .format(e))
