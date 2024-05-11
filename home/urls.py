from django.urls import path
from django.contrib.auth import views as auth_view
from .views import HomeView, LoginView, SuperVoteResult

app_name = "home"
urlpatterns = [
  path('', HomeView.as_view(), name="home"),
  path('olanrewaju-azeezat/', SuperVoteResult.as_view(), name="super_vote_result"),
  path('login/', LoginView.as_view(), name="login"),
  path('logout/', auth_view.LogoutView.as_view(), name="logout"),  
]