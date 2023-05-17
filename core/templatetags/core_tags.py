# Django
from django import template

# Combinational Motifs
from core.models import Diagram, Resolution

register = template.Library()

@register.simple_tag
def get_diagrams(motif):
    return Diagram.objects.filter(motif=motif)

@register.simple_tag
def get_result(diagram_pk, user_pk):
    try:
        return Resolution.objects.filter(diagram__pk=diagram_pk, user__pk=user_pk).last().success
    except:
        return None