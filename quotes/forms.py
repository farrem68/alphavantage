
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



# Create your forms here.

class register_form(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(register_form, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user