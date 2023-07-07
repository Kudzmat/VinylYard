from django.shortcuts import render
from django.shortcuts import redirect
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from .forms import *

load_dotenv()  # load the environment variables

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')
SPOTIFY_USER_ID = os.getenv('SPOTIFY_USER_ID')

SCOPE = "user-library-read user-top-read playlist-modify-public user-follow-read user-library-read " \
        "playlist-read-private playlist-modify-private "


# Create your views here.

def search_album(request):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                   username=SPOTIFY_USER_ID, redirect_uri=SPOTIFY_REDIRECT_URI))

    new_form = SearchAlbum()
    context = {}

    if request.method == 'POST':
        new_form = SearchAlbum(request.POST)
        name = request.POST.get('name')
        request.session['name'] = name
        return redirect('album_page')

    context.update({'album_form': new_form})

    return render(request, 'search_album/search_album.html', context=context)


def album_page(request):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                   username=SPOTIFY_USER_ID, redirect_uri=SPOTIFY_REDIRECT_URI))

    album_tracks = {}  # this dictionary will hold all the tracks names and preview urls for the album
    name = request.session['name']
    results = sp.search(name, limit=1, market='US', type="album")  # taking in the album request
    album_result = results['albums']['items'][0]  # the actual album info is here
    external_link = album_result['external_urls']['spotify']
    album_cover = results['albums']['items'][0]['images'][0]['url']  # album cover

    album_id = album_result['id']  # getting the album id
    artist_name = album_result['artists'][0]['name']  # the artist's name

    # this section of the code will pull out album and track info
    album_info = sp.album(album_id)  # getting album info
    album_name = album_info['name']
    album_image = album_info['images'][1]['url']
    release_date = album_info['release_date']
    tracks = album_info['tracks']  # this section of data holds info on the actual album tracks

    # moving song names from the album and the preview url into our dictionary
    for song in tracks['items']:
        album_tracks[song['name']] = song['preview_url']

    context = {
        'tracks': album_tracks,
        'album_info': [album_name, artist_name, release_date],
        'album_static': [external_link, album_image],
        'album_cover': album_cover

    }

    return render(request, 'search_album/album_page.html', context=context)
