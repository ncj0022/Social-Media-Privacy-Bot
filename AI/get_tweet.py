import requests
import os
import json

def getTweet(tweet_id):
    BEARER_TOKEN = os.environ.get('BEARER_TOKEN')
    if tweet_id == "":
        return
    headers = {
        'Authorization': f"Bearer {BEARER_TOKEN}",
    }
    
    raw = requests.get(f'https://api.twitter.com/2/tweets/{tweet_id}', headers=headers).text

    j_text = json.loads(raw)

    if not 'data' in j_text:
        return

    tweet = [j_text['data']['text']]
    tweet_id = [j_text['data']['id']]
    
    return ([tweet], tweet_id)

def getUser(username):
    username = username.strip('@ ')
    BEARER_TOKEN = os.environ.get('BEARER_TOKEN')
    if username == "":
        return

    headers = {
        'Authorization': f"Bearer {BEARER_TOKEN}",
    }
    
    user_data = requests.get(f'https://api.twitter.com/2/users/by/username/{username}', headers=headers)

    user_data = json.loads(user_data.text)
    if 'data' not in user_data:
        return None
    user_id = user_data['data']['id']

    params = {
        "max_results": 100
    }
    tweet_id = []
    x = json.loads(requests.get(f'https://api.twitter.com/2/users/{user_id}/tweets', params=params, headers=headers).text)
    if 'data' not in x:
        return None
    tweets = []
    for item in x['data']:
        tweets.append([item['text']])
        tweet_id.append(item['id'])
    return (tweets, tweet_id)

def getHashtag(tag):
    tag = tag.strip('#@ ')
    BEARER_TOKEN =  os.environ.get('BEARER_TOKEN')
    tweets = []
    tweet_id = []
    headers = {
        'Authorization': f"Bearer {BEARER_TOKEN}",
    }
    
    params = {
        'query': f"#{tag}",
        'max_results': 100
    }
    
    x = requests.get(f'https://api.twitter.com/2/tweets/search/recent', params=params, headers=headers)
    x = json.loads(x.text)
    truthy = True
    if 'data' not in x:
        return None
    for item in x['data']:
        tweets.append([item['text']])
        tweet_id.append(item['id'])
    if 'meta' in x:
        if 'next_token' in x['meta']:
            next_token = x['meta']['next_token']
        else:
            truthy = False
    else:
        truthy = False 
    while (truthy):
        if (len(tweets) > 4):
            truthy = False
        params.update({'next_token': next_token})
        x = requests.get(f'https://api.twitter.com/2/tweets/search/recent', params=params, headers=headers)
        x = json.loads(x.text)
        for item in x['data']:
            tweets.append([item['text']])
            tweet_id.append(item['id'])
        if 'meta' in x:
            if 'next_token' in x['meta']:
                next_token = x['meta']['next_token']
            else:
                truthy = False
        else:
            truthy = False
    
    
    return (tweets, tweet_id)
