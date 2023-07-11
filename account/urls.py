from django.urls import path
from . import views
urlpatterns = [
    path('join-member/',views.join_member, name='join_member'),
    path('success/',views.success, name='success'),
]
