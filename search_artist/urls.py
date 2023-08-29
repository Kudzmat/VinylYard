from django.urls import path
from . import views

urlpatterns = [

    path('search/', views.search_artist, name='search_artist'),
    path('page/', views.artist_page, name='artist_page')

]
