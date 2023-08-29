# VinylYard

Vinyl Yard is a Django application that allows users to interact with Spotify's API to retrieve and manipulate music data.

<img width="1344" alt="Screen Shot 2023-07-07 at 11 07 33 AM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/5ec7678a-22b1-4c4a-bdf0-bee1a430bc39">


# Features

  - Search for artists: Users can search for an artist by providing the artist’s name. The application will return the artist's page, complete with the artists picture, top tracks and albums

  - Search for album: Users can search for an album by providing the album name. The application will return relevant search results for the user to select to take you to the album page. The album page features key album information such as album name, release date, tracklist, and the option to preview album tracks.
  
- Search for tracks: Users can make use of the search feature to also look for specific tracks by entering the track name. The application will return relevant search results which the user can select from to take you to the track's album page.

  - Play music: The application provides a feature to play preview audio for selected tracks. Users can listen to a 30-second audio clip to get a preview of the track.

  - Vibe Check: Enter 5 artists you’re in the mood to listen to and the application will add 5 new songs to your Spotify playlist that align with the sound of the artists you have entered

  - Recommendations: Don’t have any artists in mind? Use the Recommendations feature and select a genre to get 5 playlist recommendations to listen to on your Spotify account

# Prerequisites

  - Python3
  -  Spotipy
  -  Django
  -  Spotify API Credentials: Obtain the client ID and client secret by creating a new app in the Spotify Developer Dashboard. Visit https://developer.spotify.com/dashboard to create a new app. https://open.spotify.com/playlist/138EKhzuYuww8DKcRC69ox?si=a47b9a69c8424cd6

# Getting Started

  - Clone The Repository
    
    ```
    $ git clone https://github.com/Kudzmat/VinylYard.git
    ```
    
  - Install and set up Django
    https://www.djangoproject.com/download/

  - Install and set up spotipy

    ```
    $ pip install spotipy
    ```
    
  - Install dependencies:
    - Set up the Spotify API credentials: Open the .env file and replace CLIENT_ID, CLIENT_SECRET, SPOTIFY_REDIRECT_URI, SPOTIFY_USER_ID and PLAYLIST_ID with your actual Spotify API credentials. To find the Spotify playlist id, go to the Spotify desktop app and enter the playlist page. Click the (...) button near the play button, and click "Copy Playlist Link" under the Share menu. The playlist id is the string right after "playlist/".
- Run the app via “python manage.py runserver” and authenticate the app to have access to your Spotify account

# Usage

The project is split into 5 apps - home_page, search_artist, search_album, search_song, and playlist.

  - # home_page:
  - This app connects users to the home page of the application where the user can access the app’s various features.

    <img width="1428" alt="Screen Shot 2023-08-29 at 11 20 59 AM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/aecf7a2b-680e-42fd-ad2a-efa133c829cc">

    Use the home page to navigate through the various features of the app


  - # search_artist:
  - This app handles all functionality involved in searching for an artist, accessing their various information, and displaying it back to the user. Enter an artist's name into the search bar and you will be taken to their page.

    <img width="1388" alt="Screen Shot 2023-08-29 at 3 45 31 PM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/c7db1ae1-bff3-4e19-9dd7-87de6efbacd1">
    
    Start with searching for an artist


    <img width="1416" alt="Screen Shot 2023-08-29 at 11 28 54 AM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/2cd6c262-87fd-49ac-b1db-b7d4c19e4279">

    Enter the artist profile and browse the top tracks...
    

    <img width="1411" alt="Screen Shot 2023-08-29 at 11 29 35 AM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/82cf0fc9-6d4e-499e-bb85-840d7512aeb2">

    Or choose from a selection of their albums...
    

    <img width="1408" alt="Screen Shot 2023-08-29 at 11 30 18 AM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/bfceaeb0-f992-4432-819c-20fab53f407d">

    Go to the album page and preview tracks from the album

    
    
  - # search_album:
  - This app handles all the functionality involved in searching for an album, accessing the album information, previewing the album tracklist, and displaying everything back to the user. Enter the name of the album you are searching for and you will be taken to the results page. Select the album you are looking for from the options available.

    <img width="1401" alt="Screen Shot 2023-08-29 at 11 31 57 AM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/154b7b13-a60d-4355-bc67-e4c2e2cd6fea">

    Search for an album

    <img width="1385" alt="Screen Shot 2023-08-29 at 11 32 50 AM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/5a89204c-3d30-4199-a39a-74c1577f3196">

    Choose your album from the selection and go to the album page


- # search_song:
- This app handles all the functionality involved in searching for a track, it returns 5 relevant search results for the user to select. Enter the name of the track you are searching for.

  <img width="1421" alt="Screen Shot 2023-08-29 at 3 57 45 PM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/84c6be46-7a2a-471b-927d-0a843c88b3d4">

  Enter the song you want to search for

  <img width="1427" alt="Screen Shot 2023-08-29 at 3 58 18 PM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/9e8e050c-a042-4dff-a1ab-2feae8928c6d">

  Select the appropriate song from the options and go to the album page



    
  - # playlist:
  - The playlist app contains all the functionality involved with playlists. It contains “Vibe Check”, where users can enter 5 artists that describe their current mood and have them added to their vibe check playlist. To make use of this feature, users must create a new playlist on their Spotify account and add the playlist ID to the .env file. To find the Spotify playlist id, go to the Spotify desktop app and enter the playlist page. Click the (...) button near the play button, and click "Copy Playlist Link" under the Share menu. The playlist id is the string right after "playlist/".


    <img width="1427" alt="Screen Shot 2023-08-29 at 11 53 56 AM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/5972b9f3-062e-405d-834b-4323756bfdd7">

    Enter 5 artists into Vibe Check

    <img width="1099" alt="Screen Shot 2023-08-29 at 4 03 28 PM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/341f33bc-a8ea-4b23-a5b1-f0d0bb7d6a58">

    Find 5 new songs added to your playlist for you to enjoy!


The playlist app also contains the genre feature, which lets a user select a genre of music from a drop-down list. The application will give the user 5 playlists to listen to full of music from the selected genre.


  <img width="1410" alt="Screen Shot 2023-08-29 at 11 45 58 AM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/5df01517-7d8d-476c-b084-8b1418862b42">

  Select a genre from the options...


  <img width="1419" alt="Screen Shot 2023-08-29 at 11 46 27 AM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/56f5d4ae-c009-4082-b7cc-814d8540c127">

  Select a playlist from the options...

  <img width="1094" alt="Screen Shot 2023-08-29 at 11 47 33 AM" src="https://github.com/Kudzmat/VinylYard/assets/65554208/4e3074f9-5235-42a0-ae5e-5c3d0b42d13e">

  Enjoy on Spotify!



# Contributions
Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.


