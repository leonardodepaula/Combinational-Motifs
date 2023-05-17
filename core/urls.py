# Django
from django.urls import path

# Views
from core.views import IndexView, ContinuousModeView, ContinuousModeResolutionView

app_name = 'core'

urlpatterns = [
    
    # Rotas
    path('',  IndexView.as_view(), name='index'),
    path('continuous/',  ContinuousModeView.as_view(), name='continuous-mode'),
    path('continuous/<int:pk>/', ContinuousModeResolutionView.as_view(), name='continuous-mode-resolution'),

]