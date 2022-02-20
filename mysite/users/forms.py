from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=32, widget=forms.TextInput(attrs={
        'class': 'input', 'placeholder': 'Username or email'
    }))
    password = forms.CharField(label='Password', min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': 'Password'
    }))

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username == password:
            raise forms.ValidationError('Username and password cannot be identical!')
        return password


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email', max_length=32, widget=forms.EmailInput(attrs={
        'class': 'input', 'placeholder': 'Email'
    }))
    password = forms.CharField(label='Password', min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': 'Password'
    }))
    password_again = forms.CharField(label='Password', min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': 'Enter password again'
    }))

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean_email(self):
        """verify if user exists"""
        email = self.cleaned_data.get('email')
        exist = User.objects.filter(email=email).exists()
        if exist:
            raise forms.ValidationError('Username already exists!')
        return email

    def clean_password_again(self):
        password = self.cleaned_data.get('password')
        password_again = self.cleaned_data.get('password_again')
        if password != password_again:
            raise forms.ValidationError('Inconsistent passwords!')
        return password_again
