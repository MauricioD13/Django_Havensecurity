"""User views"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Forms

from users.forms import SignupForm

# Create your views here.


def login_view(request):
    """Login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'users/login.html', {'error': 'Contraseña o usuario incorrecta'})
    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    """Logout user"""
    logout(request)
    return redirect('haven')


def signup(request):
    """Sign up view"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = SignupForm()

    return render(
        request=request,
        template_name='users/signup.html',
        context={'form': form}
    )
