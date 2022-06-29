import unittest

from predict import predict_text
from preprocess_flask import remove_urls, remove_emojis, remove_upper, tokens_and_punct, remove_stopwords, lemmatize_text
from get_tweet import getTweet, getUser, getHashtag

class test_test_Test(unittest.TestCase):

    def test_predict(self):
        """in this test we are determining that the predictions are consistent and returning expected results"""
        tweet_text = [['Everyone who turns on my notis will get a follow back no cap 😤🙏 #Fortnite #Fortniteleaks #FixFortnite #FortniteArt #FortniteSeason6 #FortnitePrimal #FortniteNews #fortnitecommunity #follow #followme #fortnitegfx']]
        tweet_id = ['1381942812086796288']
        self.assertEqual("""{"tweet": "1381942812086796288", "prediction": "1", "probability": 0.788406195966992}""", str(predict_text(tweet_text, tweet_id)))

    def test_empty(self):
        """in this test we are determining that when inputted with no text, error handling is correct"""
        tweet_text = [[]]
        tweet_id = ['1381942812086796288']
        self.assertEqual("""None""", str(predict_text(tweet_text, tweet_id)))

    def test_empty_tweet(self):
        """in this test we are determining that when inputted with no tweet, error handling is correct"""
        tweet = ""
        self.assertEqual("None", str(getTweet(tweet)))

    def test_empty_hash(self):
        """in this test we are determining that when inputted with no hashtag, error handling is correct"""
        tag = ""
        self.assertEqual("""None""", str(getHashtag(tag)))

    def test_empty_user(self):
        """in this test we are determining that when inputted with no username, error handling is correct"""
        user = ""
        self.assertEqual("""None""", str(getUser(user)))
    
    def test_get_tweet(self):
        """here we're going to make sure we pull the correct tweet"""
        tweet = "1385102298712395777"
        self.assertEqual("([['UNT go mean green']], ['1385102298712395777'])", str(getTweet(tweet)))

    def test_get_user(self):
        """here we're going to make sure we pull the correct tweet"""
        tweet = "programmers420"
        self.assertEqual("([['#UNT_4901_programmers We like to program'], ['UNT go mean green']], ['1385102519613890571', '1385102298712395777'])", str(getUser(tweet)))

    def test_get_hashtag(self):
        """here we're going to make sure we pull the correct tweet"""
        tweet = "UNT_4901_programmers"
        self.assertEqual("([['#UNT_4901_programmers We like to program']], ['1385102519613890571'])", str(getHashtag(tweet)))
    
    def test_remove_links(self):
        """Testing a preprocess function"""
        tweet_list = [['Everyone who turns on my notis will get a follow back no cap 😤🙏 #Fortnite #Fortniteleaks #FixFortnite #FortniteArt #FortniteSeason6 #FortnitePrimal #FortniteNews #fortnitecommunity #follow #followme #fortnitegfx']]
        tweet_list_result, tweet_links = remove_urls(tweet_list)
        compare_list = [['Everyone who turns on my notis will get a follow back no cap 😤🙏 #Fortnite #Fortniteleaks #FixFortnite #FortniteArt #FortniteSeason6 #FortnitePrimal #FortniteNews #fortnitecommunity #follow #followme #fortnitegfx']]
        compare_links = [[]]
        self.assertEqual(compare_list, tweet_list_result)
        self.assertEqual(compare_links, tweet_links)

    def test_remove_emojis(self):
        """Testing a preprocess function"""
        tweet_list = [['Everyone who turns on my notis will get a follow back no cap 😤🙏 #Fortnite #Fortniteleaks #FixFortnite #FortniteArt #FortniteSeason6 #FortnitePrimal #FortniteNews #fortnitecommunity #follow #followme #fortnitegfx']]
        tweet_list_result, tweet_emoji = remove_emojis(tweet_list)
        compare_list = [['Everyone who turns on my notis will get a follow back no cap  #Fortnite #Fortniteleaks #FixFortnite #FortniteArt #FortniteSeason6 #FortnitePrimal #FortniteNews #fortnitecommunity #follow #followme #fortnitegfx']]
        compare_emoji = [True]
        self.assertEqual(compare_list, tweet_list_result)
        self.assertEqual(compare_emoji, tweet_emoji)

    def test_remove_upper(self):
        """Testing a preprocess function"""
        tweet_list = [['Everyone who turns on my notis will get a follow back no cap #Fortnite #Fortniteleaks #FixFortnite #FortniteArt #FortniteSeason6 #FortnitePrimal #FortniteNews #fortnitecommunity #follow #followme #fortnitegfx']]
        tweet_list_result = remove_upper(tweet_list)
        compare_list = [['everyone who turns on my notis will get a follow back no cap #fortnite #fortniteleaks #fixfortnite #fortniteart #fortniteseason6 #fortniteprimal #fortnitenews #fortnitecommunity #follow #followme #fortnitegfx']]
        self.assertEqual(compare_list, tweet_list_result)

    def test_remove_tokens_and_punct(self):
        """Testing a preprocess function"""
        tweet_list = [["""WOW — what a wild double elimination! Performing arts Watch the latest episode of #TheMaskedSinger anytime: """]]
        tweet_list_result = tokens_and_punct(tweet_list)
        compare_list = [['WOW', 'what', 'a', 'wild', 'double', 'elimination', 'Performing', 'arts', 'Watch', 'the', 'latest', 'episode', 'of', 'TheMaskedSinger', 'anytime']]
        self.assertEqual(compare_list, tweet_list_result)

    def test_remove_stopwords(self):
        """Testing a preprocess function"""
        tweet_list = [['WOW', 'what', 'a', 'wild', 'double', 'elimination', 'Performing', 'arts', 'Watch', 'the', 'latest', 'episode', 'of', 'TheMaskedSinger', 'anytime']]
        tweet_list_result = remove_stopwords(tweet_list)
        compare_list = [['WOW', 'wild', 'double', 'elimination', 'Performing', 'arts', 'Watch', 'latest', 'episode', 'TheMaskedSinger', 'anytime']]
        self.assertEqual(compare_list, tweet_list_result)

    def test_lemmatize_text(self):
        """Testing a preprocess function"""
        tweet_list = [['WOW', 'what', 'a', 'wild', 'double', 'elimination', 'Performing', 'arts', 'Watch', 'the', 'latest', 'episode', 'of', 'TheMaskedSinger', 'anytime']]
        tweet_list_result = lemmatize_text(tweet_list)
        compare_list = [['WOW', 'what', 'a', 'wild', 'double', 'elimination', 'Performing', 'art', 'Watch', 'the', 'late', 'episode', 'of', 'TheMaskedSinger', 'anytime']]
        self.assertEqual(compare_list, tweet_list_result)
    

if __name__ == '__main__':
    unittest.main()