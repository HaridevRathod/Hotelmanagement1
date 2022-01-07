from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

'''
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password2')

'''
from .models import CustomerForm
 
class MyForm(forms.ModelForm):
  class Meta:
    model = CustomerForm
    fields = ["first_name", "last_name", "mobile_number", "address", "room_no", "no_of_the_days_to_stay", "date"]


#Registration Form

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
