from django.urls import path, include
from . import views

#app_name = 'search_album'
urlpatterns = [

    path('search/', views.search_album, name='search_album'),
    path('album-page/<str:name>', views.album_page, name='album_page')

]