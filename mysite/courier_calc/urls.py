from django.urls import path

from . import views

urlpatterns = [
    path('', views.calculator_home, name='calculator_home'),
]