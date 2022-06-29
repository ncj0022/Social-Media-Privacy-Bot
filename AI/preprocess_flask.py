import copy
import os
import regex
import random
import nltk
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer

#Cleaning Data functions

#Returns a URLS list from text and removes them from the list
def remove_urls(tweet_list):

    tweet_links = []
    urls = regex.compile(r'https?://\S+')
    for temp in range(0,len(tweet_list)):
        tweet_links.append(regex.findall(r'https?://\S+',tweet_list[temp][0]))

        tweet_list[temp][0] = (urls.sub(r'',tweet_list[temp][0]))
    
    return tweet_list,tweet_links

#Returns a emojis list from text and removes them from the list
def remove_emojis(tweet_list):

    tweet_emojis = []

    emojis = regex.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=regex.UNICODE)
    for temp in range(0,len(tweet_list)):
        if emojis.search(tweet_list[temp][0]) == None:
            tweet_emojis.append(False)
        else:
            tweet_emojis.append(True)
        tweet_list[temp][0] = emojis.sub(r'',tweet_list[temp][0])
    return tweet_list,tweet_emojis

# Remove upper case
def remove_upper(tweet_list):

    for num in range(0,len(tweet_list)):
        tweet_list[num][0] = tweet_list[num][0].lower()

    return tweet_list

def tokens_and_punct(tweet_list):

    #Remove all @users in text (possibly next to do hashtag)
    new_list = [regex.sub(r'@\w+', "" , y[0]) for y in tweet_list]
    token_regex = RegexpTokenizer(r'\w+')
    text_clean = [token_regex.tokenize(x) for x in new_list]
    return text_clean

def remove_stopwords(tweet_text_clean_token):
    nltk.download('stopwords')
    stop = stopwords.words('english')
    #remove text related to retweet
    stop.append("rt")
    text = [[x for x in temp if x not in stop] for temp in tweet_text_clean_token]

    return text


def get_wordnet_pos(pos_tag):
    if pos_tag.startswith('J'):
        return wordnet.ADJ
    elif pos_tag.startswith('V'):
        return wordnet.VERB
    elif pos_tag.startswith('N'):
        return wordnet.NOUN
    elif pos_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def lemmatize_text(tweet_text_clean):
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    text_lem = []
    for text in tweet_text_clean:
        pos_tags = pos_tag(text)
        text_lem.append([WordNetLemmatizer().lemmatize(t[0], get_wordnet_pos(t[1])) for t in pos_tags])
    
    return text_lem

def remove_empty_and_join(tweet_list,tweet_emojis,tweet_links,tweet_text_clean):
    count = 0
    for x in tweet_text_clean:     
        if len(x) == 0:
            del tweet_text_clean[count]
            del tweet_list[count]
            del tweet_links[count]
            del tweet_emojis[count]       
        count += 1

    #list of list: each element of list is ['text_cleaned','links','emoji_bool','label']

    final = [[clean_text,link,emoji,temp[1]] for clean_text,link,emoji,temp in zip(tweet_text_clean,tweet_links,tweet_emojis,tweet_list)]

    return final
def preprocess(tweet_input):
    
    if tweet_input == None:
        print("Error: Empty tweet_input object")
        return 

    tweet_list = copy.deepcopy(tweet_input)

    #Cleaning
    #tweet_list object = [[id,label,exists,test],....]. From the google sheet format.
    tweet_list,tweet_links = remove_urls(tweet_list)
    tweet_list,tweet_emojis = remove_emojis(tweet_list)
    tweet_list = remove_upper(tweet_list)
    tweet_text_clean_token = tokens_and_punct(tweet_list)
    tweet_text_clean = remove_stopwords(tweet_text_clean_token)
    tweet_text_clean = lemmatize_text(tweet_text_clean)
    tweet_text_clean = [" ".join(x) for x in tweet_text_clean]

    #tweet_final = [[clean_text,link,emoji] for clean_text,link,emoji in zip(tweet_text_clean,tweet_links,tweet_emojis)]
    tweet_final = [[clean_text] for clean_text in tweet_text_clean]
    #Return is list of list. Each list element is [text,links,emoji_boolean_check] for inputted data
    return tweet_final