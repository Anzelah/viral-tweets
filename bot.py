import tweepy
import config
import random

# File manipulation
def find_lyrics(file_path):
	"""A function that retrieves random lyrics from our text file. 
	It takes the file/path to file as the argument.
	"""
	with open(file_path, 'r', encoding="utf-8") as f:
		content = f.read().split('"')

        #remove extra whitespaces between lyrics
		lyrics_list = [i.strip() for i in content]

        #remove empty strings
		while('' in lyrics_list):
			lyrics_list.remove('')

        #choose random lyrics   
		lyrics = random.choice(lyrics_list)
	return lyrics

#BOT
#v2 authentication for creating tweets
client = tweepy.Client(
    consumer_key=config.consumer_key,
    consumer_secret=config.consumer_secret,
    access_token=config.access_token,
    access_token_secret=config.access_token_secret,
    wait_on_rate_limit=True
)


#post the tweets using v2 client
tweeted_lyrics = ["These are already tweeted lyrics:"]
try:
	text = find_lyrics('lyrics.txt')
	print(text)
	client.create_tweet(text=text + ' #whatsthesong')
	print('Tweet created succesfully!')

	tweeted_lyrics.append(text)
except tweepy.TweepyException as e:
	print('An error occured: {}' .format(e))


#Scheduer for when I deploy the application.
# schedule.every().day.at("10:00").do(job) 2a.m.
# schedule.every().day.at("20:00").do.(job) noon
# schedule.every().day.at("4:00").do(job) 8p.m

# while True:
    # schedule.run_pending()
    # time.sleep(1)


	