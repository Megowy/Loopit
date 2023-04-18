from django.urls import path
from search_youtube.views import SearchResultsView

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='yt_search')
]