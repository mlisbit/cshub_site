from django import forms
from models import UserProfile
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
	class Meta:
		model =  UserProfile
		fields = ('major', 'phone_number', 'user_description', 'user_avatar', 'twitter_link', 'linkedin_link', 'github_link',)
		widgets = {
            'user_avatar': forms.FileInput(attrs={'class': 'profile_pic_form'}),
      }