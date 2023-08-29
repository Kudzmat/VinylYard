from django.urls import path, include
from . import views

app_name = 'search_album'
urlpatterns = [

    path('search/', views.search_album, name='search_album'),
    path('album-results/<str:name>/', views.album_results, name='album_results'),
    path('album-page/<str:album_id>-<str:artist_name>/', views.album_page, name='album_page'),

]