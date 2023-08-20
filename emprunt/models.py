from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class EnseignantManager(BaseUserManager):
    def create_user(self, email, nom, prenom, role, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'adresse email est requise.')
        email = self.normalize_email(email)
        user = self.model(email=email, nom=nom, prenom=prenom, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nom, prenom, role='AD', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, nom, prenom, role, password, **extra_fields)


class Enseignant(AbstractBaseUser, PermissionsMixin):
    TYPE_ROLE_CHOICES = [
        ('AD', 'Admin'),
        ('PR', 'Professeur'),
    ]
    email = models.EmailField(null=True)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    role = models.CharField(max_length=2, choices=TYPE_ROLE_CHOICES)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = EnseignantManager()

    USERNAME_FIELD = 'nom'
    REQUIRED_FIELDS = ['nom', 'prenom', 'role']

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Budget(models.Model):
    TYPE_BUDGET_CHOICES = [
        ('AC', 'Année courante'),
        ('PR', 'Projets'),
        ('FE', 'Financements exceptionnels'),
    ]
    type_budget = models.CharField(max_length=2, choices=TYPE_BUDGET_CHOICES)

    def __str__(self):
        return self.type_budget


class Salle(models.Model):
    numero = models.IntegerField()

    def __str__(self):
        return str(self.numero)


class Materiel(models.Model):
    nom = models.CharField(max_length=255)
    acheteur = models.ForeignKey(Enseignant, related_name='achats', on_delete=models.CASCADE)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=True)
    proprietaire = models.ForeignKey(Enseignant, related_name='propriétés', on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, related_name='matériels', on_delete=models.CASCADE)
    possesseur = models.ForeignKey(Enseignant, related_name='possessions', on_delete=models.CASCADE)


class Accessoire(models.Model):
    ETAT_CHOICES = [
        ('NE', 'Neuf'),
        ('US', 'Usé'),
        ('EN', 'Endommagé'),
    ]
    nom = models.CharField(max_length=255)
    etat = models.CharField(max_length=2, choices=ETAT_CHOICES)
    matériel = models.ForeignKey(Materiel, related_name='accessoires', on_delete=models.CASCADE)


class Emprunt(models.Model):
    matériel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    enseignant_emprunteur = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    date_emprunt = models.DateTimeField()
    date_retour = models.DateTimeField(null=True, blank=True)
    lieu = models.CharField(max_length=255)
    occasion = models.CharField(max_length=255)
    objectif_utilisation = models.TextField()
