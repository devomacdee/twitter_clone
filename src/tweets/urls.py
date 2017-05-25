from django.conf.urls import url

from django.views.generic.base import RedirectView
from .views import (
    TweetListView,
    TweetDetailView,
    TweetCreateView,
    TweetUpdateView,
    TweetDeleteView
)

urlpatterns = [
    url(r'^$', RedirectView.as_view(url="/")), # /
    url(r'^search/$', TweetListView.as_view(), name="list"), # /tweet/search/
    url(r'^create/$', TweetCreateView.as_view(), name="create"), # /tweet/create
    url(r'^(?P<pk>\d+)$', TweetDetailView.as_view(), name="detail"), #/tweet/1
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name="update"), #/tweet/update
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name="delete"), #/tweet/delete
]
