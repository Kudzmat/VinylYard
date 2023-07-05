from django.urls import path, include
from . import views

urlpatterns = [

    path('vibe-check', views.vibe_check, name='vibe_check'),
    path('add-vibe', views.add_vibe, name='add_vibe')

]