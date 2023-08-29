from django.urls import path, include
from . import views

app_name = 'search_song'
urlpatterns = [

    path('search/', views.search_track, name='search_track'),
    path('results/<str:name>/', views.track_results, name='track_results')

]