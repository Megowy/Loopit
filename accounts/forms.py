from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = CustomUser.objects.filter(username=username)
        if new.count():
            print("User Already Exist")
            raise ValidationError("User Already Exist")
        return username

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = CustomUser.objects.filter(email=email)
        if new.count():
            print(" Email Already Exist")
            raise ValidationError(" Email Already Exist")
        return email

    def clean_password(self):
        password = self.cleaned_data['password1']
        if len(password) < 8:
            print("password is too short")
            raise ValidationError("password is too short")
        return password

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            print("Password don't match")
            raise ValidationError("Password don't match")
        return password2


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

def clean_password(self):
  password = self.cleaned_data['password']
  if len(password) < 8:
      print("password is too short")
      raise ValidationError("password is too short")
  return password