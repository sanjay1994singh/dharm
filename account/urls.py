from django.urls import path

from . import views

urlpatterns = [
    path('join-member/', views.join_member, name='join_member'),
    path('add-member/<int:id>/', views.add_member, name='add_member'),
    path('free-member/', views.free_member, name='free_member'),

    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-conditions/', views.terms_conditions, name='terms_conditions'),
    path('cancellation-refund/', views.cancellation_refund, name='cancellation_refund'),
    path('shipping-delivery/', views.shipping_delivery, name='shipping_delivery'),
]
