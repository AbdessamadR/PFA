from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),  # Route pour la page d'accueil
    path('login/', views.login_view, name='login'),
    path('register/client/', views.register_client, name='register_client'),
    path('register/restaurant/', views.register_restaurant, name='register_restaurant'),
    path('register/livreur/', views.register_livreur, name='register_livreur'),
    path('client/dashboard/', views.dashboard_client, name='dashboard_client'),
    path('restaurant/dashboard/', views.dashboard_restaurant, name='dashboard_restaurant'),
    path('livreur/dashboard/', views.dashboard_livreur, name='dashboard_livreur'),
    path('logout/', LogoutView.as_view(), name='logout'),  # Déconnexion
]
