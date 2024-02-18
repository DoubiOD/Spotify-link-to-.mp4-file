from __future__ import unicode_literals
import sys, spotipy, yt_dlp, ffmpeg

from spotipy.oauth2 import SpotifyClientCredentials
from selenium import webdriver
from selenium.webdriver.common.by import By

client_id, client_secret = 'client_id', 'client_secret'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }],
}

def get_track_name(spotify_track_link):

    track_id = spotify_track_link.split('/')[-1]
    track_info = sp.track(track_id)
    track_name = track_info['name']
    artist_name = track_info['artists'][0]['name']

    return track_name + artist_name

def p(search_query):
    final_query, link = "", []
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    for word in search_query:
        final_query += word

    print("final_query: " + final_query)
        
    driver.get('https://www.youtube.com/results?search_query={}'.format(final_query))
    select = driver.find_element(By.CSS_SELECTOR, 'div#contents ytd-item-section-renderer>div#contents a#thumbnail')
    link += [select.get_attribute('href')]

    print("link: " + link[0])
    return link[0]

def download_from_url(track_link):
    ydl.download([track_link])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <spotify_track_link>")
        sys.exit(1)

    track_link = p(get_track_name(sys.argv[1]))
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        download_from_url(track_link)
