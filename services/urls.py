from django.urls import path

from . import views

urlpatterns = [
    path('puja_form/', views.puja_form, name='puja_form'),
    path('Jyotish_form/', views.Jyotish_form, name='Jyotish_form'),
]
