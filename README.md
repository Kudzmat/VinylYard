# VinylYard

Vinyl Yard is a Django application that allows users to interact with Spotify's API to retrieve and manipulate music data.

<img width="1344" alt="Screen Shot 2023-07-07 at 11 07 33 AM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/5ec7678a-22b1-4c4a-bdf0-bee1a430bc39">


# Features

  - Search for artists: Users can search for an artist by providing the artist’s name. The application will return a list of matching tracks along with relevant information such as the track name, artist, and albums.

  - Search for album: Users can search for an album by providing the album name. The application will return the key album information such as album name, tracklist, and the option to preview album tracks.

  - Play music: The application provides a feature to play preview audio for selected tracks. Users can listen to a 30-second audio clip to get a preview of the track.

  - Vibe Check: Enter 5 artists you’re in the mood to listen to and the application will add 5 new songs to your Spotify playlist that align with the sound of the artists you have entered

  - Recommendations: Don’t have any artists in mind? Use the Recommendations feature and select a genre to get 5 playlists recommendations to listen to on your Spotify account

# Prerequisites

  - Python3
  -  Spotipy
  -  Django
  -  Spotify API Credentials: Obtain the client ID and client secret by creating a new app in the Spotify Developer Dashboard. Visit https://developer.spotify.com/dashboard to create a new app. https://open.spotify.com/playlist/138EKhzuYuww8DKcRC69ox?si=a47b9a69c8424cd6

 <img width="1355" alt="Screen Shot 2023-07-07 at 6 22 48 PM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/77f3e785-1311-47df-a11f-f09a7dde3da8">


# Getting Started

  - Clone The Repository
  - Install and set up Django
  - Install dependencies:
    - Set up the Spotify API credentials: Open the .env file and replace CLIENT_ID, CLIENT_SECRET, SPOTIFY_REDIRECT_URI, SPOTIFY_USER_ID and PLAYLIST_ID with your actual Spotify API credentials. To find the Spotify playlist id, go to the Spotify desktop app and enter the playlist page. Click the (...) button near the play button, and click "Copy Playlist Link" under the Share menu. The playlist id is the string right after "playlist/".
- Run the app via “python manage.py runserver” and authenticate the app to have access to your Spotify account

<img width="1357" alt="Screen Shot 2023-07-08 at 3 57 44 PM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/0c8fcaaf-fba0-4043-90f9-18eabb4b968f">


# Usage

The project is split into 4 apps - home_page, search_artist, search_album, and playlist.

  - home_page: This app connects users to the home page of the application where the user can access the app’s various features.
  - search_artist: This app handles all functionality involved in searching for an artist, accessing their various information, and displaying it back to the user.
  - search_album: This app handles all the functionality involved in searching for an album, accessing the album information, previewing the album tracklist, and displaying everything back to the user.
  - playlist: The playlist app contains all the functionality involved with playlists. It contains “Vibe Check”, where users can enter 5 artists that describe their current mood and have them added to a playlist of their choosing. It also contains the genre playlist feature, this lets a user select a genre of music from a drop-down list. The application will give the user 5 playlists to listen to full of music from the selected genre.

<img width="1361" alt="Screen Shot 2023-07-07 at 6 21 07 PM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/bc471c45-1b45-4ac4-8a8b-963033973140">


# Contributions
Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.


