from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=20,
        help_text="Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only."
    )
    email = forms.EmailField(help_text="Required. Email must end with '@student.gsu.edu'")
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email.endswith('@student.gsu.edu'):
            raise ValidationError(f"Email must end with '@student.gsu.edu'")
        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']