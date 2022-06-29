import tweepy

# Authenticate to Twitter
#auth = tweepy.OAuthHandler()
#auth.set_access_token()

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

search_words = "#GameDevelopment" #Whatever your hashtag is
date_since = "2018-11-16"

tweets = tweepy.Cursor(api.search, q = search_words, lang="en", since=date_since).items(10)

for tweet in tweets:
    print(tweet.id)

for tweet in tweets:
    print(tweet.tweet)