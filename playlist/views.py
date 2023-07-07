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
PLAYLIST_ID = os.getenv('PLAYLIST_ID')

SCOPE = "user-library-read user-top-read playlist-modify-public user-follow-read user-library-read " \
        "playlist-read-private playlist-modify-private "


def add_vibe(request):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                   username=SPOTIFY_USER_ID, redirect_uri=SPOTIFY_REDIRECT_URI))

    new_form = VibeCheck()
    artist_list = []  # each artist will be appended to this list
    context = {}

    if request.method == 'POST':
        new_form = VibeCheck(request.POST)

        artist1 = request.POST.get('artist1')
        artist_list.append(artist1)

        artist2 = request.POST.get('artist2')
        artist_list.append(artist2)

        artist3 = request.POST.get('artist3')
        artist_list.append(artist3)

        artist4 = request.POST.get('artist4')
        artist_list.append(artist4)

        artist5 = request.POST.get('artist5')
        artist_list.append(artist5)

        request.session['artist_list'] = artist_list
        return redirect('vibe_check')  # redirect to vibe_check

    context.update({'vibe_form': new_form})

    return render(request, 'playlist/vibe_check.html', context=context)


def vibe_check(request):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                   username=SPOTIFY_USER_ID, redirect_uri=SPOTIFY_REDIRECT_URI))

    playlist_name = 'Vibe Check'
    playlist_id = PLAYLIST_ID
    artists_ids = []  # the recommended artist's IDs will be added to this list
    tracks = []  # the recommended tracks will be added to this list
    artist_list = request.session['artist_list']  # calling the artist list from the previous route
    print(artist_list)

    # getting the playlist we want to add the songs to
    playlists = sp.user_playlists(user=SPOTIFY_USER_ID)  # all playlists
    for item in playlists['items']:
        print(item['name'])
        print(item['id'])

    # putting artist ids in a list
    for artist in artist_list:
        name_result = sp.search(artist, limit=1, type='artist', market='US')
        artist_info = name_result['artists']['items'][0]  # get artist ID
        artist_id = artist_info['id']
        artists_ids.append(artist_id)

    # getting 5 song recommendation and appending them to the tracks list
    result = sp.recommendations(seed_artists=artists_ids, limit=5, country='US')
    for item in result['tracks']:
        tracks.append(item['uri'])  # track['uri']

    sp.playlist_add_items(playlist_id=playlist_id, items=[song for song in tracks])  # adding songs

    return redirect('https://open.spotify.com/playlist/138EKhzuYuww8DKcRC69ox')  # takes you to playlist page


def genre_playlist(request):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                   username=SPOTIFY_USER_ID, redirect_uri=SPOTIFY_REDIRECT_URI))

    genre_form = GenrePickForm()
    context = {}

    if request.method == 'POST':
        genre_form = GenrePickForm(request.POST)

        selected_genre = request.POST.get('genre')
        return redirect('get_playlists', selected_genre=selected_genre)

    context.update({'genre_form': genre_form})

    return render(request, 'playlist/genre_playlist.html', context=context)


def get_playlists(request, selected_genre):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                   username=SPOTIFY_USER_ID, redirect_uri=SPOTIFY_REDIRECT_URI))

    categories = {}  # will hold music categories and playlist ids
    recommendations = {}  # will hold playlist name, image, link and description

    tunes = sp.categories(country='US')  # get category list
    tunes1 = tunes['categories']['items']  # gives us access to genre & id keys

    for item in tunes1:
        # setting our items to variables
        genre = item['name']
        genre_id = item['id']

        # adding items to dictionary
        categories[genre] = genre_id

    # search for category in dictionary
    if selected_genre in categories.keys():

        # get playlist id using dictionary key (category)
        playlist_id = categories[selected_genre]

        # get 5 playlist recommendations
        playlists = sp.category_playlists(category_id=playlist_id, limit=5)

    else:
        # take back to home page if we don't get 5 playlists or if the category is missing from the dictionary
        return redirect("home_page:home")

    # getting access to our essential information
    play_list_info = playlists['playlists']['items']

    for info in play_list_info:
        # setting our information to variables
        playlist_name = info['name']
        description = info['description']
        link = info['external_urls']['spotify']
        image = info['images'][0]['url']

        # adding our information using the playlist name as a key and a list of the other info as value
        recommendations[playlist_name] = [description, link, image]

    context = {
        'recommendations': recommendations,
        'selected_genre': selected_genre
    }

    return render(request, "playlist/get_playlists.html", context=context)
