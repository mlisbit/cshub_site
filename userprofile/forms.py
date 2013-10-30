from django import forms
from models import UserProfile, Clubs
from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple


class UserProfileForm(forms.ModelForm):
	class Meta:
		model =  UserProfile
		fields = ('major', 'phone_number', 'user_description', 'user_avatar', 'twitter_link', 'linkedin_link', 'github_link', 'student_number', 'school', 'public_email',)
		widgets = {
            'user_avatar': forms.FileInput(attrs={'class': 'profile_pic_form'}),
      }
