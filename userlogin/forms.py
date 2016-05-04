from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.hashers import PBKDF2PasswordHasher,SHA1PasswordHasher
from django.contrib.auth.forms import UserCreationForm

class Login(forms.Form):
    username=forms.CharField(label='Username',max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
            
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email',)
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("The Username Already Exists")
        else:
            return username
            
        
    #def clean_password(self):
     #   password = self.cleaned_data.get('password')
      #  if len(password) >= 8:
       #     return make_password(password, salt=None, hasher='default')
        #else:
         #   raise forms.ValidationError("The password shoul be min 8 char long")
