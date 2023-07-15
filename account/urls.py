from django.urls import path
from . import views
urlpatterns = [
    path('join-member/',views.join_member, name='join_member'),
    path('add-member/<int:id>/',views.add_member, name='add_member'),
    path('free-member/',views.free_member, name='free_member'),
    path('success/',views.success, name='success'),
]
