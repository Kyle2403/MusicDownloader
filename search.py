#!/usr/bin/python
# You must provide a developer key obtained
# in the Google APIs Console. Search for "REPLACE_ME" in this code
# to find the correct place to provide that key..
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Set DEVELOPER_KEY to the API key value from 
# https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = 'AIzaSyDJvYgdBFg52GFWzGUQzL9iwC-xIIMqNDs'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search():
  q = input("What do you want to search?\n>> ")
  if q == "": q = "game"
  max_results = input("What is the maximum number of results you want?\n>> ")
  try:
    max_results = int(max_results)
  except Exception:
    print("The maximum number is not an integer, set to 10 as default")
    max_results = 10  
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(q=q,part='id,snippet',maxResults=max_results).execute()

  videos = []
  channels = []
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      # call videos().list() to get the duration of a search result using its ID
      video_response = youtube.videos().list(id=search_result['id']['videoId'],part = 'contentDetails').execute()
      video = video_response.get('items',[])[0]
      
      # get the duration and do some cleaning
      duration = video['contentDetails']['duration'].replace("PT","").replace("H",":").strip("S").replace("M",":")
      title = search_result['snippet']["title"]
      channel_title = search_result['snippet']["channelTitle"]
      id = search_result['id']['videoId']
      vid = [title,id,duration,channel_title]
      videos.append(vid)

    elif search_result['id']['kind'] == 'youtube#channel':
      channel = [search_result['snippet']["title"],search_result['id']['channelId']]
      channels.append(channel)
    elif search_result['id']['kind'] == 'youtube#playlist':
      playlist = [search_result['snippet']["title"],search_result['id']['playlistId']]
      playlists.append(playlist)
  
  return videos, channels, playlists


def show(videos):
  if len(videos) == 0:
    print("-------------------No Results--------------------")
    return
  i = 1
  print("-------------------Results--------------------")
  for video in videos:
    print("Number {}: {} || (Posted by {}) (Length: {})".format(i,video[0],video[3],video[2]))
    i += 1
  print("-------------------Results--------------------")

