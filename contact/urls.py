from django.urls import path
from .views import contact_form, success

urlpatterns = [
    path('contact/',contact_form, name='contact'),
    path('success/', success, name='success')
]
