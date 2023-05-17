# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Django Packages
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

# Combinational Motifs
from core.models import User, Motif, Diagram, Resolution

@admin.register(User)
class UserAdminModel(admin.ModelAdmin):
    model = User

@admin.register(Motif)
class MotifAdminModel(TreeAdmin):
    form = movenodeform_factory(Motif)

@admin.register(Diagram)
class DiagramAdminModel(admin.ModelAdmin):
    model = Diagram

@admin.register(Resolution)
class ResolutionAdminModel(admin.ModelAdmin):
    model = Resolution
