from django import forms
from models import Comment, Event, Going

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment 
		fields = ('body',)

class GoingForm(forms.ModelForm):
	class Meta:
		model = Going 