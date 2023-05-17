# Django
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

# Dango Packages
from treebeard.ns_tree import NS_Node

# Combinational Motifs
from core.managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=100, unique=True, verbose_name='Username')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Motif(NS_Node):

    name = models.CharField(max_length=500, verbose_name='Motif name')
    start = models.IntegerField(verbose_name='Start index')
    stop = models.IntegerField(verbose_name='Stop index')

    class Meta:
        verbose_name = 'Motif'
        verbose_name_plural = 'Motifs'
    
    def __str__(self):
        return str(self.name)
    
class Diagram(models.Model):

    motif = models.ForeignKey('core.Motif', related_name='motifs', on_delete=models.PROTECT, verbose_name='Motif')
    index = models.IntegerField(verbose_name='Index')

    class Meta:
        verbose_name = 'Diagram'
        verbose_name_plural = 'Diagrams'
    
    def __str__(self):
        return f'{self.motif.name} - Diagram {self.index}'

class Resolution(models.Model):

    diagram = models.ForeignKey('core.Diagram', related_name='diagrams', on_delete=models.PROTECT, verbose_name='Diagram')
    user = models.ForeignKey('core.User', related_name='users', on_delete=models.PROTECT, verbose_name='User')
    date = models.DateTimeField(default=timezone.now, verbose_name='Date')
    success = models.BooleanField(verbose_name='Success')

    class Meta:
        verbose_name = 'Resolution'
        verbose_name_plural = 'Resolutions'
    
    def __str__(self):
        return f'{self.diagram} - Success: {self.success}'