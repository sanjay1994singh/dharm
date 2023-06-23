from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('service_details/<int:id>/',views.service_details,name='service_details'),
    path('biography/<int:id>/',views.biography,name='biography'),
    path('add-gallery/',views.add_gallery,name='add_gallery'),
    path('gallery/',views.gallery,name='gallery'),
]