from django.urls import path

from . import views
# 8899956789
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('harame_stambh/', views.harame_stambh, name='harame_stambh'),
    path('dharm_kya_hai/', views.dharm_kya_hai, name='dharm_kya_hai'),
    path('contact/', views.contact, name='contact'),
    path('service_details/<int:id>/', views.service_details, name='service_details'),
    path('biography/<int:id>/', views.biography, name='biography'),
    path('add-gallery/', views.add_gallery, name='add_gallery'),

    path('gallery/', views.gallery, name='gallery'),
    path('photo-gallery/', views.photo_gallery, name='photo_gallery'),
    path('image_folder/<int:id>/', views.image_folder, name='photo_gallery'),
    path('samachar-gallery/', views.samachar_gallery, name='photo_gallery'),
    path('viewPdf1/', views.viewPdf1, name='viewPdf1'),
    path('viewPdf2/', views.viewPdf2, name='viewPdf2'),
    path('sangthan/', views.sangthan_suchi, name='sangthan_suchi'),
    path('get_sangth_padname/', views.get_sangth_padname, name='get_sangth_padname'),
    path('get_sangth/', views.get_sangth, name='get_sangth'),
    path('sangthan_list/<int:id>/', views.sangthan_list, name='sangthan_list'),

    path('add_gallery_folder/', views.add_gallery_folder, name='add_gallery_folder'),
    path('video-gallery/', views.videos_list, name='videos_list'),
]
