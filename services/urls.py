from django.urls import path

from . import views

urlpatterns = [
    path('jyotish/', views.jyotish, name='jyotish'),

    path('dharm_sandesh/', views.dharm_sandesh, name='dharm_sandesh'),
    path('dharmik_ayojan/', views.dharmik_ayojan, name='dharmik_ayojan'),
    path('rajat_shila/', views.rajat_shila, name='rajat_shila'),
    path('braj_yatra/', views.braj_yatra, name='braj_yatra'),
    path('braj_yatra_place/<int:id>/', views.braj_yatra_place, name='braj_yatra_place'),
    path('temple_details/<int:id>/', views.temple_details, name='temple_details'),
    path('daan/', views.daan, name='daan'),

    path('jyotish_samadhan/', views.jyotish_samadhan, name='jyotish_samadhan'),
    path('helpline/', views.helpline, name='helpline'),
]
