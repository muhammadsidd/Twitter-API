import tweepy
import time
consumer_key = 'enterkey'
consumer_secret = 'enter secret key'
key = 'enter token'
secret = 'enter secret token'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
#api.update_status('Twitter bot reporting in live ')

user = "elonmusk"
num = 100
FILE_NAME = 'last_seen.txt'

def readlastseen(FILE_NAME):
    file_read = open(FILE_NAME,'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def writelastseen(FILE_NAME, last):
    file_write = open(FILE_NAME,'w')
    file_write.write(str(last))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(readlastseen(FILE_NAME))

    for tweet in reversed(tweets):
        
        print(str(tweet.id)+'--'+tweet.text)
        api.update_status("@" + tweet.user.screen_name + " ya'll fucking insane", tweet.id)
        api.create_favorite(tweet.id)
        api.retweet(tweet.id)
        writelastseen(FILE_NAME, tweet.id)

def search(name,numberoftweets):
    fleets = tweepy.Cursor(api.user_timeline, name).items(numberoftweets)
    for fleet in fleets:
        try:
            fleet.retweet()
            print("DONE RETWEETING " + fleet.text)
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

while True:
    reply()
    search(user,num)
    




