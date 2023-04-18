from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django import forms
from django.forms import CharField, EmailField, PasswordInput
from django.core.exceptions import ValidationError
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    username = CharField(label='username', min_length=6, max_length=32)
    email = EmailField(label='email')
    password1 = CharField(label='password', widget=PasswordInput)
    password2 = CharField(label='Confirm password', widget=PasswordInput)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = CustomUser.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = CustomUser.objects.filter(email=email)
        if new.count():
            raise ValidationError(" Email Already Exist")
        return email

    def clean_password(self):
        password = self.cleaned_data['password1']
        if len(password) < 8:
            raise ValidationError("password is too short")
        return password

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self):
        user = CustomUser.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password1'])
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

def clean_password(self):
  password = self.cleaned_data['password']
  if len(password) < 8:
      raise ValidationError("password is too short")
  return password