from django.shortcuts import render
from django.shortcuts import redirect
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from .forms import TrackSearchForm
import pprint

load_dotenv()  # load the environment variables

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')
SPOTIFY_USER_ID = os.getenv('SPOTIFY_USER_ID')

SCOPE = "user-library-read user-top-read playlist-modify-public user-follow-read user-library-read " \
        "playlist-read-private playlist-modify-private "


def search_track(request):

    form = TrackSearchForm()
    context = {}

    if request.method == 'POST':
        form = TrackSearchForm(request.POST)
        name = request.POST.get('track_name')
        return redirect('search_song:track_results', name=name)  # redirect to results page

    context.update({'form': form})

    return render(request, 'search_song/search_song.html', context=context)


def track_results(request, name):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                   username=SPOTIFY_USER_ID, redirect_uri=SPOTIFY_REDIRECT_URI))

    # search for track
    tracks = sp.search(q=name, type='track', limit=5, market='US')
    results = {}

    track_info = tracks['tracks']

    for i in range(5):
        song_preview = track_info['items'][i]['preview_url']
        song_name = track_info['items'][i]['name']
        song_art = track_info['items'][i]['album']['images'][1]['url']
        artist_name = track_info['items'][i]['artists'][0]['name']
        song_id = track_info['items'][i]['album']['id']

        results[song_id] = [artist_name, song_art, song_name, song_preview]

    #pprint.pprint(results)

    context = {'results': results,
               'name': name}

    return render(request, 'search_song/song_results.html', context=context)


