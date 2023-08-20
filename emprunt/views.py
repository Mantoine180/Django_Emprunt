from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import EnseignantLoginForm


# Create your views here.

def index(request):
    return render(request, 'base.html')


def login_view(request):
    if request.method == "POST":
        form = EnseignantLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('nom_de_votre_vue_après_connexion')
    else:
        form = EnseignantLoginForm()

    return render(request, 'Registration/login.html', {'form': form})