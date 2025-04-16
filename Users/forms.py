from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class ClientRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name','telephone']  # Pas de champ `role` ici

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = CustomUser.CLIENT  # Attribuer le rôle 'restaurant' automatiquement
        if commit:
            user.save()
        return user



class RestaurantRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name','image']  # Pas de champ `role` ici

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = CustomUser.RESTAURANT  # Attribuer le rôle 'restaurant' automatiquement
        if commit:
            user.save()
        return user

class LivreurRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'vehicule', 'numero_permis']# Pas de champ `role` ici

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = CustomUser.LIVREUR  # Attribuer le rôle 'livreur' automatiquement
        if commit:
            user.save()
        return user
