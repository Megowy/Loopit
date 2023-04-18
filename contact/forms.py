from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    email = forms.CharField(validators=[EmailValidator()], required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)