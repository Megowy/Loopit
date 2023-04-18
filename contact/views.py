from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ["megowy@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def success(request):
   return render(request, 'success.html')