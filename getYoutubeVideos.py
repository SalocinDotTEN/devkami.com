import urllib
import json

api_key = "AIzaSyBNdaGj26VeSj-WkNd9GVs0wc9gtqLjS4I"
channel_id = "UCMs8l2DQ7S6tiBDBSn_4isA"

base_video_url = 'https://www.youtube.com/watch?v='
base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

first_url = base_search_url + \
    'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(
        api_key, channel_id)

video_links = []
url = first_url
while True:
    inp = urllib.urlopen(url)
    resp = json.load(inp)

    print(resp)

    for i in resp['items']:
        if i['id']['kind'] == "youtube#video":
            video_links.append(base_video_url + i['id']['videoId'])

    try:
        next_page_token = resp['nextPageToken']
        url = first_url + '&pageToken={}'.format(next_page_token)
    except:
        break

print(video_links)
