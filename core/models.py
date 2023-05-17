# Django
from django.db import models

# Dango Packages
from treebeard.ns_tree import NS_Node

# Combinational Motifs
from core.mixins import NSNodeMixin

class Motif(NS_Node):

    name = models.CharField(max_length=500, verbose_name='Motif name')
    start = models.IntegerField(verbose_name='Start index')
    stop = models.IntegerField(verbose_name='Stop index')

    class Meta:
        verbose_name = 'Motif'
        verbose_name_plural = 'Motifs'
    
    def __str__(self):
        return str(self.name)