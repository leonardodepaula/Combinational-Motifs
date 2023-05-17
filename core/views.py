# Django
from django.views.generic import TemplateView

# Combinational Motifs
from core.models import Motif

class IndexView(TemplateView):

    template_name = 'core/index.html'

class ContinuousModeView(TemplateView):

    template_name = 'core/continuous.html'

    def get_context_data(self, **kwargs):
        context = super(ContinuousModeView, self).get_context_data(**kwargs)

        context['motifs'] = Motif.objects.all()

        return context