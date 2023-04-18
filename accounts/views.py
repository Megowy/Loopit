from django.contrib.auth import login, get_user_model
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView


# Create your views here.
User = get_user_model()


class CustomLoginView(LoginView):
    template_name = "login.html"
    fields = "__all__"
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    success_url = reverse_lazy("index")


def register(request):
    if request.POST == 'POST':
        form = CustomUserCreationForm()
        if form.is_valid():
            form.save()
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'register.html', context)

# class RegisterView(FormView):
#     template_name = "register.html"
#     form_class = CustomUserCreationForm
#     redirect_authenticated_user = True
#     success_url = reverse_lazy("index")
#
#     def form_valid(self, form):
#         user = form.save()
#         if user is not None:
#             login(self.request, user)
#         return super(RegisterView, self).form_valid(form)
#
#     def get(self, *arg, **kwargs):
#         if self.request.user.is_authenticated:
#             return redirect("index")
#         return super(RegisterView, self).get(*arg, **kwargs)

