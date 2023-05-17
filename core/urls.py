# Django
from django.urls import path

# Views
from core.views import IndexView, ContinuousModeView, ContinuousModeResolutionView, ResultView, UserRegisterView, UserLoginView, UserLogoutView

app_name = 'core'

urlpatterns = [
    
    # Rotas
    path('',  IndexView.as_view(), name='index'),
    path('login/',  UserLoginView.as_view(), name='login'),
    path('logout/',  UserLogoutView.as_view(), name='logout'),
    path('register/',  UserRegisterView.as_view(), name='register'),
    path('continuous/',  ContinuousModeView.as_view(), name='continuous-mode'),
    path('continuous/<int:pk>/', ContinuousModeResolutionView.as_view(), name='continuous-mode-resolution'),
    path('result/', ResultView.as_view(), name='result'),

]