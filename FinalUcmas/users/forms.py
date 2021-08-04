from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    username=forms.CharField(max_length=50)
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=254,help_text="Required, write a valid email address")
    password1=forms.PasswordInput()
    password2=forms.PasswordInput()
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        # StudentImage=forms.FileField()
        # BirthDate = forms.DateField(required=False,  input_formats=settings.DATE_INPUT_FORMATS)
        fields = ['user','StudentFirstName', 'StudentMiddleName','StudentLastName','StudentEmail','BirthDate','Gender', 'std','Enroll', 'SchoolName', 'Hobbies', 'Refference', 'Ressidence']

