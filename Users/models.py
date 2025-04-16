# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    CLIENT = 'client'
    RESTAURANT = 'restaurant'
    LIVREUR = 'livreur'

    ROLE_CHOICES = [
        (CLIENT, 'Client'),
        (RESTAURANT, 'Restaurant'),
        (LIVREUR, 'Livreur'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    # Champs communs ou spécifiques :
    # Champs pour les restaurants :
    nom_restaurant = models.CharField(max_length=100, null=True, blank=True)
    adresse = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='restaurants/', null=True, blank=True)

    # Champs pour les livreurs :
    vehicule = models.CharField(max_length=50, null=True, blank=True)
    numero_permis = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.username
