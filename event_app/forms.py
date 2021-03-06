from django import forms
from models import Comment, Event, Going

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment 
		fields = ('body',)
		widgets = {'body': forms.TextInput(attrs={'class': 'comment_form', 'placeholder': 'Type comment here...'}),}

class GoingForm(forms.ModelForm):
	class Meta:
		model = Going 