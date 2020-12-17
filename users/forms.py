from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm (UserCreationForm):
	email = forms.EmailField()

	# Provides a nested namespace for configuration and keeps the configurations in one place, aka only affecting the User model
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	# Provides a nested namespace for configuration and keeps the configurations in one place, aka only affecting the User model
	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']