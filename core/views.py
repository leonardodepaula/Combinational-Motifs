# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, TemplateView


# Combinational Motifs
from core.models import Motif, Diagram

class IndexView(TemplateView):

    template_name = 'core/index.html'

class ContinuousModeView(LoginRequiredMixin, TemplateView):

    template_name = 'core/continuous.html'

    def get_context_data(self, **kwargs):
        context = super(ContinuousModeView, self).get_context_data(**kwargs)

        context['motifs'] = Motif.objects.all()

        return context

class ContinuousModeResolutionView(LoginRequiredMixin, DetailView):

    context_object_name = 'diagram'
    model = Diagram
    template_name = 'core/resolution.html'

    def get_context_data(self, **kwargs):
        context = super(ContinuousModeResolutionView, self).get_context_data(**kwargs)

        return context