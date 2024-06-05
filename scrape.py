import tweepy

consumer_key = 'XXXX'
consumer_secret = 'XXXX'
access_token = 'XXXX'
access_token_secret = 'XXXX'

#Pass our twitter credentials to tweepy authentication handler
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)

#Instantiate the tweepy api using our credentials
api = tweepy.API(auth)

#Main app now
try:
	user = api.get_user(screen_name="jack")
	print('{}' .format(user.screen_name))
	print('{}' .format(user.followers_count))
except tweepy.TweepyException as e:
	print('An error occured: {}' .format(e))



if __name__ == "__main__":
	print('Hello world!')