# Django
from django import template

# Combinational Motifs
from core.models import Diagram

register = template.Library()

@register.simple_tag
def get_diagrams(motif):
    return Diagram.objects.filter(motif=motif)