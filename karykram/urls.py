from django.urls import path

from . import views

urlpatterns = [
    path('<str:type>/', views.karykram, name='karykram'),
]
