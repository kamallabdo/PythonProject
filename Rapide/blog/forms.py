from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	CIN = forms.CharField(max_length=8)
	class Meta:
		model = User
		fields = ["CIN",'password1','email']