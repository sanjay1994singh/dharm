from django.urls import path

from . import views

urlpatterns = [
    path('join-member/', views.join_member, name='join_member'),
    path('add-member/<str:type>/', views.add_member, name='add_member'),
    path('हितचिंतक-सदस्य/', views.free_member, name='free_member'),

    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-conditions/', views.terms_conditions, name='terms_conditions'),
    path('cancellation-refund/', views.cancellation_refund, name='cancellation_refund'),
    path('shipping-delivery/', views.shipping_delivery, name='shipping_delivery'),

    path('sadasya_list1/', views.sadasya_list1, name='sadasya_list1'),
    path('sadasya_list2/', views.sadasya_list2, name='sadasya_list2'),
    path('sadasya_list3/', views.sadasya_list3, name='sadasya_list3'),

    path('certificate_genrate/<int:id>/', views.certificate_genrate, name='certificate_genrate'),
]
