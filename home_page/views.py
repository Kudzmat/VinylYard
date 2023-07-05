from django.shortcuts import render
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()  # load the environment variables

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')
SPOTIFY_USER_ID = os.getenv('SPOTIFY_USER_ID')

SCOPE = "user-library-read user-top-read playlist-modify-public user-follow-read user-library-read " \
        "playlist-read-private playlist-modify-private "


# home page
def index(request):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                   username=SPOTIFY_USER_ID, redirect_uri=SPOTIFY_REDIRECT_URI))

    new_releases = sp.new_releases(country='US', limit=5)
    albums = new_releases['albums']['items']

    song_name1 = albums[0]['name']
    image1 = albums[0]['images'][1]['url']
    artist_name1 = albums[0]['artists'][0]['name']
    link1 = albums[0]['external_urls']['spotify']

    song_name2 = albums[1]['name']
    image2 = albums[1]['images'][1]['url']
    artist_name2 = albums[1]['artists'][0]['name']
    link2 = albums[1]['external_urls']['spotify']

    song_name3 = albums[2]['name']
    image3 = albums[2]['images'][1]['url']
    artist_name3 = albums[2]['artists'][0]['name']
    link3 = albums[2]['external_urls']['spotify']

    song_name4 = albums[3]['name']
    image4 = albums[3]['images'][1]['url']
    artist_name4 = albums[3]['artists'][0]['name']
    link4 = albums[3]['external_urls']['spotify']

    song_name5 = albums[4]['name']
    image5 = albums[4]['images'][1]['url']
    artist_name5 = albums[4]['artists'][0]['name']
    link5 = albums[4]['external_urls']['spotify']

    new_music = {
        song_name1: [link1, image1, artist_name1],
        song_name2: [link2, image2, artist_name2],
        song_name3: [link3, image3, artist_name3],
        song_name4: [link4, image4, artist_name4],
        song_name5: [link5, image5, artist_name5]
    }

    context = {
        'albums': new_music,
    }

    return render(request, 'home_page/index.html', context=context)
