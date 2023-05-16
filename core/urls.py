# Django
from django.urls import path

# Views
from core.views import *

app_name = 'core'

urlpatterns = [
    
    # Rotas
    path('',  IndexView.as_view(), name='index'),

]