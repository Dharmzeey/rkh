from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from .models import *
from .forms import *


class VoteHomePage(View):
  template_name = "vote/homepage.html"
  def get(self, request):
    return render(request, self.template_name)
  
  
class Vote(LoginRequiredMixin, View):
  template_name = "vote/vote.html"
  voted_template_name = "vote/vote-success.html"
  def get(self, request):
    if request.user.is_voted:
      return render(request, self.voted_template_name)
    hall_chair_aspirants = HallChairman.objects.all()
    vice_hall_chair_aspirants = ViceHallChairman.objects.all()
    gen_sec_aspirants = GeneralSecretary.objects.all()
    # fin_sec_aspirants = FinancialSecretary.objects.all()
    info_aspirants = InformationMinister.objects.all()
    defense_aspirants = InternalAffairsAndDefenseMinister.objects.all()
    health_aspirants = HealthMinister.objects.all()
    sport_aspirants = SportMinister.objects.all()
    # social_aspirants = SocialAndWelfareMinister.objects.all()
    src_aspirants = StudentRepresentativeCouncil.objects.all()    
    
    hall_chair_form = HallChairmanForm()
    vice_hall_chair_form = ViceHallChairmanForm()
    gen_sec_form = GeneralSecretaryForm()
    # fin_sec_form = FinancialSecretaryForm()
    info_form = InformationMinisterForm()
    defense_form = InternalAffairsDefenseMinisterForm()
    health_form = HealthMinisterForm()
    sport_form = SportMinisterForm()
    # social_form = SocialAndWelfareMinisterForm()
    src_form = StudentRepresentativeCouncilForm()
    data = {
      "hall_chair_form": hall_chair_form,
      "vice_hall_chair_form": vice_hall_chair_form,
      "gen_sec_form": gen_sec_form,
      "info_form": info_form,
      "defense_form": defense_form,
      "health_form": health_form,
      "sport_form": sport_form,
      "src_form": src_form,
      
      "hall_chair_aspirants": hall_chair_aspirants,
      "vice_hall_chair_aspirants": vice_hall_chair_aspirants,
      "gen_sec_aspirants": gen_sec_aspirants,
      "info_aspirants": info_aspirants,
      "defense_aspirants": defense_aspirants,
      "health_aspirants": health_aspirants,
      "sport_aspirants": sport_aspirants,
      "src_aspirants": src_aspirants,
    }
    return render(request, self.template_name, data)
  
  def post(self, request):
    if request.user.is_voted:
      return render(request, self.voted_template_name)
    hall_chair_form = HallChairmanForm(request.POST) 
    vice_hall_chair_form = ViceHallChairmanForm(request.POST)
    gen_sec_form = GeneralSecretaryForm(request.POST)
    # fin_sec_form = FinancialSecretaryForm(request.POST)
    info_form = InformationMinisterForm(request.POST)
    defense_form = InternalAffairsDefenseMinisterForm(request.POST)
    health_form = HealthMinisterForm(request.POST)
    sport_form = SportMinisterForm(request.POST)
    # social_form = SocialAndWelfareMinisterForm(request.POST)
    src_form = StudentRepresentativeCouncilForm(request.POST)
    
    if hall_chair_form.is_valid() and vice_hall_chair_form.is_valid() and gen_sec_form.is_valid() and  info_form.is_valid() and defense_form.is_valid() and health_form.is_valid() and sport_form.is_valid() and src_form.is_valid():
      voter = request.user
      form = hall_chair_form.save(commit=False)
      form.voter = voter
      form.save()
      form = vice_hall_chair_form.save(commit=False)
      form.voter = voter
      form.save()
      form = gen_sec_form.save(commit=False)
      form.voter = voter
      form.save()
      form = info_form.save(commit=False)
      form.voter = voter
      form.save()
      form = defense_form.save(commit=False)
      form.voter = voter
      form.save()
      form = health_form.save(commit=False)
      form.voter = voter
      form.save()
      form = sport_form.save(commit=False) 
      form.voter = voter
      form.save()
      form = src_form.save(commit=False)     
      form.voter = voter
      form.save()
      src_form.save_m2m() # saves the m2m
      # Change the vote status to True
      voter.is_voted = True
      voter.save()
      return render(request, self.voted_template_name)
    return render(request, self.template_name)