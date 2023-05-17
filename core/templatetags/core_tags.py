# Django
from django import template

# Combinational Motifs
from core.models import Diagram, Resolution

register = template.Library()

@register.simple_tag
def get_diagrams(motif):
    return Diagram.objects.filter(motif=motif)

@register.simple_tag
def get_result(diagram, user):
    try:
        return Resolution.objects.filter(diagram=diagram, user=user).last().success
    except:
        return None