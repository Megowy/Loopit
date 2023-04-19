from django.contrib import admin
from django.urls import path
from app_player.views import PlayerView, SongCreateView, SongUpdateView, SongDeleteView
from app_player.views import looper, index, looper_basic, add_part, delete_part, save_video

from app_player.models import Song, Part


admin.site.register(Song)  # appear in admin form after registration
admin.site.register(Part)

urlpatterns = [
    path('', index, name='index'),
    path('songs_list', PlayerView.as_view(), name='songs_list'),
    path('song/add_song', SongCreateView.as_view(), name='add_song'),
    path('song/update_song/<pk>', SongUpdateView.as_view(), name='update_song'),
    path('song/delete_song/<pk>', SongDeleteView.as_view(), name='delete_song' ),
    path('add_part/<song_url>', add_part, name = 'add_loop'),
    path('delete_part/<id>', delete_part, name = 'delete_loop'),
    path('looper/<pk>', looper, name='looper'),
    path('looper_basic/<video_url>', looper_basic, name='looper_basic'),
    path('save_video/<video_url>', save_video, name='save_video'),
    path('', PlayerView.as_view(), name='index'),

]
