from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('signup/', SignUpAPI.as_view(), name='signup'),
    path('login/', SignUpAPI.as_view(), name='login'),
    path('logout/', SignUpAPI.as_view(), name='logout'),
    path('spotify-login/', spotify_login, name='spotify-login'),
    path('spotify-callback/', spotify_callback, name='spotify-callback'),
    path('diary/', DiaryEntryAPI.as_view(), name='diary-entry'),
    path('diary/list/', DiaryListAPI.as_view(), name='diary-list'),
    path('mood-playlists/', MoodPlaylistAPI.as_view(), name='mood-playlists'),
    
]