from django import forms
from .models import *
from user.models import StudentRepresentativeCouncil

class HallChairmanForm(forms.ModelForm):
  class Meta:
    model = HallChairmanVote
    fields = "hall_chairman",
    widgets = {
      "hall_chairman": forms.RadioSelect,
    }
    
class ViceHallChairmanForm(forms.ModelForm):
  class Meta:
    model = ViceHallChairmanVote
    fields = "vice_hall_chairman",
    widgets = {
      "vice_hall_chairman": forms.RadioSelect,
    }
    
class GeneralSecretaryForm(forms.ModelForm):
  class Meta:
    model = GeneralSecretaryVote
    fields = "general_secretary",
    widgets = {
      "general_secretary": forms.RadioSelect,
    }
    
class FinancialSecretaryForm(forms.ModelForm):
  class Meta:
    model = FinancialSecretaryVote
    fields = "financial_secretary",
    widgets = {
  "financial_secretary": forms.RadioSelect,
}

    
class InformationMinisterForm(forms.ModelForm):
  class Meta:
    model = InformationMinisterVote
    fields = "information_minister",
    widgets = {
  "information_minister": forms.RadioSelect,
}

    
class InternalAffairsDefenseMinisterForm(forms.ModelForm):
  class Meta:
    model = InternalAffairsAndDefenseMinisterVote
    fields = "internal_affairs_and_defense_minister",
    widgets = {
  "internal_affairs_and_defense_minister": forms.RadioSelect,
}

    
class HealthMinisterForm(forms.ModelForm):
  class Meta:
    model = HealthMinisterVote
    fields = "health_minister",
    widgets = {
  "health_minister": forms.RadioSelect,
}

    
class SportMinisterForm(forms.ModelForm):
  class Meta:
    model = SportMinisterVote
    fields = "sport_minister",
    widgets = {
  "sport_minister": forms.RadioSelect,
}

    
class SocialAndWelfareMinisterForm(forms.ModelForm):
  class Meta:
    model = SocialAndWelfareMinisterVote
    fields = "social_and_welfare_minister",
    widgets = {
  "social_and_welfare_minister": forms.RadioSelect,
}

    
class StudentRepresentativeCouncilForm(forms.ModelForm):
  
  # student_representative_council = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=StudentRepresentativeCouncil.objects.all())
  class Meta:
    model = StudentRepresentativeCouncilVote
    fields = "student_representative_council",
    widgets = {
      "student_representative_council": forms.CheckboxSelectMultiple,
    }
