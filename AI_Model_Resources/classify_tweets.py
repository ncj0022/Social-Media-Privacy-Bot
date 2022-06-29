import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import requests
import json

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)
sheet = client.open("tweets").sheet1 # Open the spreadhseet


def get_tweet(tweet_id):
    BEARER_TOKEN = "xxxxxxxxxx"

    headers = {
        'Authorization': f"Bearer {BEARER_TOKEN}",
    }
    ids = ",".join(tweet_id)
    ids = f"{len(tweet_id)},{ids}"
    params = {
        'ids': ids
    }
    return requests.get('https://api.twitter.com/2/tweets', params=params, headers=headers)


rows = {}
x = sheet.range('A65001:D65532')
tweet_ids = []

for cell in range(0, len(x)-1):
    if isinstance(x[cell], str):
        continue
    if x[cell].col != 1:
        continue
    else:
        tweet_ids.append(x[cell].value)
        rows.update({
            x[cell].value: {
                "exists": x[cell+2],
                "text": x[cell+3]
            }
        })

responses = []

final_tweet_ids = [tweet_ids[i * 99:(i + 1) * 99] for i in range((len(tweet_ids) + 99 - 1) // 99 )]
count = 0
for item in final_tweet_ids:
    count += 1
    try:
        if count == 300:
            print(count)
            break
        response = get_tweet(item)
        responses.append(response.text)
    except Exception as e:
        break
cells = []
for response in responses:
    data = json.loads(response)
    for item in data['data']:
        if item['id'] not in rows:
            continue
        rows[item['id']]['exists'].value = "Yes"
        rows[item['id']]['text'].value = item['text']
        cells.append(rows[item['id']]['exists'])
        cells.append(rows[item['id']]['text'])
    for item in data['errors']:
        if item['value'] not in rows:
            continue
        rows[item['value']]['exists'].value = "No"
        cells.append(rows[item['value']]['exists'])
    print(len(cells))
sheet.update_cells(cells)