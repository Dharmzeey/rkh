from django.urls import path
from .views import *

app_name = "vote"
urlpatterns = [
  # path('', VoteHomePage.as_view(), name="homepage"),
  path('', Vote.as_view(), name="vote"),
  
]