from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('home_page.urls')),
    path('artist/', include('search_artist.urls')),
    path('album/', include('search_album.urls')),
    path('playlist-corner/', include('playlist.urls')),
]
