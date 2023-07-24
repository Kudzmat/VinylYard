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
        return redirect('search_album:album_results', name=name)  # redirect to results page

    context.update({'album_form': new_form})

    return render(request, 'search_album/search_album.html', context=context)


# 5 search results will be displayed to the user
def album_results(request, name):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                   username=SPOTIFY_USER_ID, redirect_uri=SPOTIFY_REDIRECT_URI))

    album_list = {}  # will hold each individual album and the info I need

    albums = sp.search(q=name, limit=5, type='album', market='US')
    album2 = albums['albums']

    # get artist names and album information and put them in a dictionary
    for i in range(5):
        artist_name = album2['items'][i]['artists'][0]['name']
        album_name = album2['items'][i]['name']
        album_id = album2['items'][i]['id']  # album ID is a unique album identifier so we will use it as the key
        album_image = album2['items'][i]['images'][1]['url']

        album_list[album_id] = [album_name, artist_name, album_image]

    context = {'results': album_list,
               'name': name
               }

    return render(request, 'search_album/results.html', context=context)


# the album display page with track previews and other information
def album_page(request, album_id, artist_name):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                   username=SPOTIFY_USER_ID, redirect_uri=SPOTIFY_REDIRECT_URI))

    album_tracks = {}  # this dictionary will hold all the tracks names and preview urls for the album
    artist_name = artist_name  # the artist's name

    # this section of the code will pull out album and track info
    album_info = sp.album(album_id)  # getting album info
    album_name = album_info['name']
    album_cover = album_info['images'][0]['url']
    album_image2 = album_info['images'][1]['url']
    spotify_link = album_info['external_urls']['spotify']
    release_date = album_info['release_date']
    tracks = album_info['tracks']  # this section of data holds info on the actual album tracks

    # moving song names from the album and the preview url into our dictionary
    for song in tracks['items']:
        album_tracks[song['name']] = song['preview_url']

    context = {
        'tracks': album_tracks,
        'album_info': [album_name, artist_name, release_date],
        'album_static': [spotify_link, album_image2],
        'album_cover': album_cover

    }

    return render(request, 'search_album/album_page.html', context=context)
