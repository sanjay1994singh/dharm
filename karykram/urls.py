from django.urls import path

from . import views

urlpatterns = [
    path('karykram/<str:type>/', views.karykram, name='karykram'),
]
