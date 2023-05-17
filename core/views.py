# Django
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView, View, FormView


# Combinational Motifs
from core.forms import UserForm
from core.models import Motif, Diagram, User, Resolution

class IndexView(FormView):

    template_name = 'core/index.html'
    form_class = AuthenticationForm

class UserRegisterView(FormView):

    template_name = 'core/register.html'
    form_class = UserForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            login(request=self.request, user=user, backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponseRedirect(reverse_lazy('core:index'))
        else:
            return self.form_invalid(form)

class UserLoginView(LoginView):

    form_class = AuthenticationForm

class UserLogoutView(LogoutView):
    pass

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