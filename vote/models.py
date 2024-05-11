from django.db import models
from user.models import *

# Create your models here.

class HallChairmanVote(models.Model):
  voter = models.OneToOneField(User, on_delete=models.CASCADE)
  hall_chairman = models.ForeignKey(HallChairman, on_delete=models.SET_NULL, null=True)
  time_voted = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return f" {self.hall_chairman.name} - {self.voter.email}"

class ViceHallChairmanVote(models.Model):
  voter = models.OneToOneField(User, on_delete=models.CASCADE)
  vice_hall_chairman = models.ForeignKey(ViceHallChairman, on_delete=models.SET_NULL, null=True)
  time_voted = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return f" {self.vice_hall_chairman.name} - {self.voter.email}"
  
class GeneralSecretaryVote(models.Model):
  voter = models.OneToOneField(User, on_delete=models.CASCADE)
  general_secretary = models.ForeignKey(GeneralSecretary, on_delete=models.SET_NULL, null=True)
  time_voted = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return f" {self.general_secretary.name} - {self.voter.email}"
  
class FinancialSecretaryVote(models.Model):
  voter = models.OneToOneField(User, on_delete=models.CASCADE)
  financial_secretary = models.ForeignKey(FinancialSecretary, on_delete=models.SET_NULL, null=True)
  time_voted = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return f" {self.financial_secretary.name} - {self.voter.email}"  
  
class InformationMinisterVote(models.Model):
  voter = models.OneToOneField(User, on_delete=models.CASCADE)
  information_minister = models.ForeignKey(InformationMinister, on_delete=models.SET_NULL, null=True)
  time_voted = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return f" {self.information_minister.name} - {self.voter.email}"  
  
class InternalAffairsAndDefenseMinisterVote(models.Model):
  voter = models.OneToOneField(User, on_delete=models.CASCADE)
  internal_affairs_and_defense_minister = models.ForeignKey(InternalAffairsAndDefenseMinister, on_delete=models.SET_NULL, null=True)
  time_voted = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return f" {self.internal_affairs_and_defense_minister.name} - {self.voter.email}"  
  
class HealthMinisterVote(models.Model):
  voter = models.OneToOneField(User, on_delete=models.CASCADE)
  health_minister = models.ForeignKey(HealthMinister, on_delete=models.SET_NULL, null=True)
  time_voted = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return f" {self.health_minister.name} - {self.voter.email}"  
  
class SportMinisterVote(models.Model):
  voter = models.OneToOneField(User, on_delete=models.CASCADE)
  sport_minister = models.ForeignKey(SportMinister, on_delete=models.SET_NULL, null=True)
  time_voted = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return f" {self.sport_minister.name} - {self.voter.email}"  
  
class SocialAndWelfareMinisterVote(models.Model):
  voter = models.OneToOneField(User, on_delete=models.CASCADE)
  social_and_welfare_minister = models.ForeignKey(SocialAndWelfareMinister, on_delete=models.SET_NULL, null=True)
  time_voted = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return f" {self.social_and_welfare_minister.name} - {self.voter.email}"  
  
class StudentRepresentativeCouncilVote(models.Model):
  voter = models.OneToOneField(User, on_delete=models.CASCADE)
  student_representative_council = models.ManyToManyField(StudentRepresentativeCouncil)
  time_voted = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return f" {self.voter.email}"  