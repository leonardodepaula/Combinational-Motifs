# Django
from django.contrib import admin

# Django Packages
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

# Combinational Motifs
from core.models import Motif

@admin.register(Motif)
class MotifAdmin(TreeAdmin):
    form = movenodeform_factory(Motif)