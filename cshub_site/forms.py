from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	class Meta: 
		model = User
		fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email')	

	email = forms.CharField(help_text=None)
	username = forms.CharField(help_text=None)
	#password2 = forms.CharField(help_text=None)

	
	def clean_email(self):
		from django.core.validators import validate_email
		try:
			validate_email(self.cleaned_data.get('email'))
		except:
			raise forms.ValidationError("Invalid email.") 
		return self.cleaned_data.get('email')

	def clean_username(self):
	    username = self.cleaned_data["username"]
	    restricted_usernames = ['admin', 'administrator']
	    if username.lower() in restricted_usernames:
	    	raise forms.ValidationError("Restricted username") 
	    try:
	        User._default_manager.get(username=username)
	    except User.DoesNotExist:
	        return username
	    raise forms.ValidationError(
	        self.error_messages['duplicate_username'],
	        code='duplicate_username',
	    )
	    return username
	
	def clean_last_name(self):
		first_name = self.cleaned_data.get("first_name")
		last_name = self.cleaned_data.get("last_name")
		if first_name == last_name:
			raise forms.ValidationError("Must differ from first.") 
		return last_name
		
	def save(self, commit=True):
		user = super(MyRegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']

		if (commit == True):
			user.save()

		return user

class ContactForm(forms.Form):
	title = forms.CharField(max_length=20)
	email = forms.CharField(max_length=20)
	text = forms.CharField(widget = forms.Textarea)

	def clean_email(self):
		from django.core.validators import validate_email
		try:
			validate_email(self.cleaned_data.get('email'))
		except:
			raise forms.ValidationError("Invalid email.") 

	def clean_text(self):
		cd = self.cleaned_data
		text = cd.get('text')

		banned_words = ['viagra', 'casino', 'href=']
		for x in banned_words:
			if x in text:
				raise forms.ValidationError("Some of these words are banned.") 