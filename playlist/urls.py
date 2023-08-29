from django.urls import path, include
from . import views

urlpatterns = [

    path('vibe-check', views.vibe_check, name='vibe_check'),
    path('add-vibe', views.add_vibe, name='add_vibe'),
    path('pick-genre', views.genre_playlist, name='genre_playlist'),
    path('get-playlist/<str:selected_genre>/', views.get_playlists, name='get_playlists'),

]