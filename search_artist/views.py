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

# will take you to the artist form page
def search_artist(request):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                   username=SPOTIFY_USER_ID, redirect_uri=SPOTIFY_REDIRECT_URI))

    new_form = SearchArtist()
    context = {}

    if request.method == 'POST':
        new_form = SearchArtist(request.POST)
        name = request.POST.get('name')
        request.session['name'] = name
        return redirect('artist_page')

    context.update({'artist_form': new_form})

    return render(request, 'search_artist/search_artist.html', context=context)


# will take you to that specific artist's home page
def artist_page(request):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                   username=SPOTIFY_USER_ID, redirect_uri=SPOTIFY_REDIRECT_URI))

    album_names = {}  # will hold album names and images, this dictionary will prevent duplicates
    top_songs = {}  # will hold the artists top 5 songs

    name = request.session['name']
    name_result = sp.search(name, limit=1, type='artist', market='US')  # searching for the artist
    artist_display = name_result['artists']['items'][0]
    artist_name = artist_display['name']
    artist_followers = "{:,}".format(artist_display['followers']['total'])  # formatting for large numbers
    artist_genres = artist_display['genres']

    # artist display images
    large_image = name_result['artists']['items'][0]['images'][0]['url']
    med_image = name_result['artists']['items'][0]['images'][1]['url']

    # getting top songs. We will only display the top 8 tracks on the page
    artist_info = name_result['artists']['items'][0]  # get artist ID
    artist_id = artist_info['id']
    # use ID to find top tracks
    top_tracks = sp.artist_top_tracks(artist_id)

    # search for albums using artist ID
    album_results = sp.artist_albums(artist_id=artist_id, country='US', limit=20)
    album_results = album_results['items']  # items holds all the album objects

    # this section will prevent the app from showing duplicate albums
    for album in album_results:
        if len(album_names) == 5:  # we only want to display 5 albums
            break
        else:
            if album['name'] not in album_names:
                album_names[album['name']] = album['images'][0]['url']
            else:
                pass

    # getting top songs
    for song in top_tracks['tracks'][:5]:
        top_songs[song['name']] = song['album']['images'][2]['url']

    context = {
        'info': album_names,
        'name': artist_name,
        'songs': top_songs,
        'large_image': large_image,
    }

    return render(request, 'search_artist/artist_page.html', context=context)
