# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView, RedirectView, View


# Combinational Motifs
from core.models import Motif, Diagram, User, Resolution

class IndexView(RedirectView):

    url = reverse_lazy('core:continuous-mode')

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

class ResultView(LoginRequiredMixin, View):

    def post(self, *args, **kwargs):
        user = User.objects.get(pk=self.request.POST.get('user'))
        diagram = Diagram.objects.get(pk=self.request.POST.get('diagram'))
        result = self.request.POST.get('result')

        if result == 'success':
            success = True
        else:
            success = False

        Resolution.objects.create(user=user, diagram=diagram, success=success)

        return HttpResponse(result)