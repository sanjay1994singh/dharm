from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_pradesh, name='all_pradesh'),
    path('pradesh_list/<int:id>/', views.pradesh_list, name='pradesh_list'),
    path('district_list/<int:id>/', views.district_list, name='district_list'),
    path('nagar_list/<int:id>/', views.nagar_list, name='nagar_list'),
]
