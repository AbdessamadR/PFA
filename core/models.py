from django.db import models
from django.conf import settings

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='produits/')  # champ image
    stock = models.PositiveIntegerField(default=0)
    disponible = models.BooleanField(default=True)
    categorie = models.CharField(max_length=100, blank=True)
    restaurant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='produits')

    def __str__(self):
        return self.nom


class Commande(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='commandes')
    adresse_livraison = models.CharField(max_length=255)
    date_commande = models.DateTimeField(auto_now_add=True)
    mode_paiement = models.CharField(
        max_length=20,
        choices=[('en ligne', 'En ligne'), ('livraison', 'Paiement à la livraison')],
        default='livraison'
    )
    instructions = models.TextField(blank=True)
    statut = models.CharField(max_length=20, default='en attente')

    def __str__(self):
        return f"Commande #{self.id} - {self.client.username}"


class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='lignes')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom}"


class Livraison(models.Model):
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE)
    livreur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='livraisons')
    adresse_livraison = models.CharField(max_length=255)
    date_livraison = models.DateTimeField(null=True, blank=True)
    numero_suivi = models.CharField(max_length=100, blank=True)
    statut = models.CharField(max_length=20, default='en attente')

    def __str__(self):
        return f"Livraison de {self.commande} par {self.livreur.username}"
