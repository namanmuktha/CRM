from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record 

from django import forms 

from django.contrib.auth.forms import AuthenticationForm 
from django.forms.widgets import   PasswordInput, TextInput
# -Register a User 

class CreateUserForm(UserCreationForm):

    class Meta :

        model = User 
        fields = ['username','password1','password2']

# login  a user 

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
#Adding leads
class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = Record 
        fields = ['first_name','last_name','email','phone','address','city','provience']

#Updating Leads 
class UpdateRecordForm(forms.ModelForm):

    class Meta:

        model = Record 
        fields = ['first_name','last_name','email','phone','address','city','provience']
