from django import forms
from user.models import User

class LoginForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ("email", "password")
  password = forms.CharField(
  widget=forms.PasswordInput(render_value=True))