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
    
<img width="1359" alt="Screen Shot 2023-07-21 at 8 06 58 PM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/d337a337-9b3f-4bed-8f4a-0e4068cd0e6b">



# Getting Started

  - Clone The Repository
    $ git clone https://github.com/Kudzmat/VinylYard.git
    
  - Install and set up Django
    https://www.djangoproject.com/download/

  - Install and set up spotipy
    $ pip install spotipy
    
  - Install dependencies:
    - Set up the Spotify API credentials: Open the .env file and replace CLIENT_ID, CLIENT_SECRET, SPOTIFY_REDIRECT_URI, SPOTIFY_USER_ID and PLAYLIST_ID with your actual Spotify API credentials. To find the Spotify playlist id, go to the Spotify desktop app and enter the playlist page. Click the (...) button near the play button, and click "Copy Playlist Link" under the Share menu. The playlist id is the string right after "playlist/".
- Run the app via “python manage.py runserver” and authenticate the app to have access to your Spotify account

<img width="1357" alt="Screen Shot 2023-07-21 at 8 14 05 PM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/4b2a8903-d1f0-40be-b44f-123c509eebc7">



# Usage

The project is split into 4 apps - home_page, search_artist, search_album, and playlist.

  - home_page: This app connects users to the home page of the application where the user can access the app’s various features.

  - search_artist: This app handles all functionality involved in searching for an artist, accessing their various information, and displaying it back to the user. Enter an artist's name into the search bar and you will be taken to their page.

    <img width="1350" alt="Screen Shot 2023-07-23 at 8 48 10 PM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/2fa08fd1-85f8-4b2a-9745-e500dcf1b4e6">
    Browse the top tracks for an artist...

    <img width="1361" alt="Screen Shot 2023-07-23 at 8 49 54 PM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/44cdf804-9604-44c4-b97d-8fa23ef85e4e">
    Or choose from a select of their albums.


    
  - search_album: This app handles all the functionality involved in searching for an album, accessing the album information, previewing the album tracklist, and displaying everything back to the user. Enter the name of the album you are searching for and you will be taken to the results page. Select the album you are looking for from the options available.

    <img width="1345" alt="Screen Shot 2023-07-24 at 4 07 55 PM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/f529a296-676e-44f8-bd0b-09084178f390">
  Find the album you are looking for and select it....

  <img width="1357" alt="Screen Shot 2023-07-24 at 2 46 42 PM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/526223f7-177f-468f-9a69-f5d985aa1db4">
  Go to the album page and preview the album tracklist.


    
  - playlist: The playlist app contains all the functionality involved with playlists. It contains “Vibe Check”, where users can enter 5 artists that describe their current mood and have them added to their vibe check playlist. To make use of this feature, users must create a new playlist on their spotify account and add the playlist ID to the .env file. To find the Spotify playlist id, go to the Spotify desktop app and enter the playlist page. Click the (...) button near the play button, and click "Copy Playlist Link" under the Share menu. The playlist id is the string right after "playlist/".

    <img width="1345" alt="Screen Shot 2023-07-24 at 4 07 55 PM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/f826a5fe-20f2-48bf-a3a2-9e8be69ad47a">

    
    


The playlist app also contains the genre feature, which lets a user select a genre of music from a drop-down list. The application will give the user 5 playlists to listen to full of music from the selected genre.

<img width="1326" alt="Screen Shot 2023-07-23 at 8 54 07 PM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/41ed6c1e-425b-4db7-abba-b4ff92ea4267">



# Contributions
Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.


