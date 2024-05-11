from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.shortcuts import HttpResponseRedirect, render, redirect
from django.urls import reverse
from django.views import View
from django.db.models import Count
from django.db.models.functions import Coalesce
from vote import models as vote_model
from user import models as user_model
from vote.models import *
from user.models import User
from .forms import LoginForm


# Create your views here.

class SuperVoteResult(LoginRequiredMixin, View):
  template_name = "home/vote-result.html"
  def get(self, request):
    if not request.user.is_superuser:
      return redirect(reverse('vote:vote'))
    
    hall_chair_votes = HallChairman.objects.annotate(vote_count=Coalesce(Count('hallchairmanvote'), 0))
    vice_hall_chair_votes = ViceHallChairman.objects.annotate(vote_count=Coalesce(Count('vicehallchairmanvote'), 0))
    gen_sec_votes = GeneralSecretary.objects.annotate(vote_count=Coalesce(Count('generalsecretaryvote'), 0))
    info_votes = InformationMinister.objects.annotate(vote_count=Coalesce(Count('informationministervote'), 0))
    defense_votes = InternalAffairsAndDefenseMinister.objects.annotate(vote_count=Coalesce(Count('internalaffairsanddefenseministervote'), 0))
    health_votes = HealthMinister.objects.annotate(vote_count=Coalesce(Count('healthministervote'), 0))
    sport_votes = SportMinister.objects.annotate(vote_count=Coalesce(Count('sportministervote'), 0))
    src_votes = StudentRepresentativeCouncil.objects.all()  
    for i in src_votes  :
      print(i.studentrepresentativecouncilvote_set.count())

    data = {
      "hall_chair_votes": hall_chair_votes,
      "vice_hall_chair_votes": vice_hall_chair_votes,
      "gen_sec_votes": gen_sec_votes,
      "info_votes": info_votes,
      "defense_votes": defense_votes,
      "health_votes": health_votes,
      "sport_votes": sport_votes,
      "src_votes": src_votes,
    }
    return render(request, self.template_name, data) 

class HomeView(View):
  template_name = "home/home.html"
  def get(self, request):
    # if request.user.is_authenticated:
    #   return HttpResponseRedirect(reverse('vote:vote'))
    eligible_voters= User.objects.all().count()
    total_votes = HallChairmanVote.objects.all().count()
    data = {
      "eligible_voters": eligible_voters,
      "total_votes": total_votes
    }
    return render(request, self.template_name, data)
  

class LoginView(View):
  template_name = "home/login.html"
  def get(self, request):
    if request.user.is_authenticated:
      return redirect(reverse('vote:vote'))
    data = {"form": LoginForm()}
    return render(request, self.template_name, data)
  
  def post(self, request):
    if request.user.is_authenticated:
      return HttpResponseRedirect(reverse('vote:vote'))
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
      if user.is_voted:
        return render(request, 'home/voted.html')
      elif not user.is_voted:
        login(request, user)
        return HttpResponseRedirect(reverse('vote:vote'))
    else:
      data = {"form": LoginForm(), 'error': 'Invalid email and password combination'}
      return render(request, self.template_name, data)
    
