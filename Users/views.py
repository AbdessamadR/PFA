from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import ClientRegisterForm, RestaurantRegisterForm, LivreurRegisterForm

# ===== Page d'accueil =====
def home(request):
    return render(request, 'comptes/home.html')  # Page d'accueil simple

# ===== Connexion =====
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirection selon le rôle
            if user.role == 'client':
                return redirect('dashboard_client')
            elif user.role == 'restaurant':
                return redirect('dashboard_restaurant')
            elif user.role == 'livreur':
                return redirect('dashboard_livreur')
    else:
        form = AuthenticationForm()
    return render(request, 'comptes/login.html', {'form': form})

# ===== Inscriptions =====
def register_client(request):
    if request.method == 'POST':
        form = ClientRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Sauvegarder l'utilisateur avec le rôle 'client'
            return redirect('login')  # Redirection vers la page de login
    else:
        form = ClientRegisterForm()
    return render(request, 'comptes/register_client.html', {'form': form})

def register_restaurant(request):
    if request.method == 'POST':
        form = RestaurantRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Sauvegarder l'utilisateur avec le rôle 'restaurant'
            return redirect('login')  # Redirection vers la page de login
    else:
        form = RestaurantRegisterForm()
    return render(request, 'comptes/register_restaurant.html', {'form': form})

def register_livreur(request):
    if request.method == 'POST':
        form = LivreurRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Sauvegarder l'utilisateur avec le rôle 'livreur'
            return redirect('login')  # Redirection vers la page de login
    else:
        form = LivreurRegisterForm()
    return render(request, 'comptes/register_livreur.html', {'form': form})

# ===== Dashboards =====
@login_required
def dashboard_client(request):
    if request.user.role != 'client':
        return HttpResponseForbidden("Accès refusé")
    return render(request, 'comptes/dashboard_client.html')

@login_required
def dashboard_restaurant(request):
    if request.user.role != 'restaurant':
        return HttpResponseForbidden("Accès refusé")
    return render(request, 'comptes/dashboard_restaurant.html')

@login_required
def dashboard_livreur(request):
    if request.user.role != 'livreur':
        return HttpResponseForbidden("Accès refusé")
    return render(request, 'comptes/dashboard_livreur.html')


