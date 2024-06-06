import tweepy
import config


client = tweepy.Client(
    consumer_key=config.consumer_key,
    consumer_secret=config.consumer_secret,
    access_token=config.access_token,
    access_token_secret=config.access_token_secret
)
client.create_tweet(text='Testing tweepy.')

#try:
#	api.update_status("testing tweepy")
#	print('Tweet posted successfully')
#except tweepy.TweepyException as e:
#	print('An error occured: {}' .format(e))
