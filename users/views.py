"""User views"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

# Forms

from users.forms import SignupForm

# Create your views here.

class LoginView(auth_views.LoginView):
    """Login View

    Args:
        auth_views ([type]): [description]
    """
    
    template_name = 'users/login.html'
    

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    
    template_name = 'users/logout.html'
    
    next_page = 'haven'



class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


