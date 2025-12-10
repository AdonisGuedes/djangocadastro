from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar, name='home'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', views.login, name='login'),
]